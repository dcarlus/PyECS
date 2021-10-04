import pygame
from ecs.components import Component, ComponentFactory
from ecs.entities import Entity
from ecs.systems import SystemProcessing, System
from game.components.engine.positioncomponent import Point
from game.appdata import AppData, SystemName
from engine.graphics.sprite import Sprite

class SpriteComponent(Component):
    """Component containing the graphics elements for drawing an animated item (character, monster, other)."""

    def __init__(self, entity: Entity) -> None:
        """Create a new SpriteComponent instance."""
        super().__init__(entity)
        self.m_sprite: Sprite = Sprite()

    @property
    def sprite(self) -> Sprite:
        """Get the Sprite of the Component."""
        return self.m_sprite

    @sprite.setter
    def sprite(self, sprite: Sprite) -> None:
        """Set the Sprite of the Component."""
        self.m_sprite = sprite


class SpriteProcessing(SystemProcessing):
    """System processing of SpriteComponents."""

    def __init__(self, components: ComponentFactory):
        """Create a new SpriteProcessing instance."""
        super().__init__(components)
        self.m_spriteGroup = pygame.sprite.Group()

    def onDelete(self, entity: Entity) -> None:
        """Do something when an entity is removed."""
        spriteComponent: SpriteComponent = self.m_components.components(entity)[0]
        self.m_spriteGroup.remove(spriteComponent.sprite)

    def pre(self, linkedSystems: {str, System}) -> [Entity]:
        """Prepare work before run."""
        spriteComponentsList: [SpriteComponent] = self.m_components.allComponents()
        positionSystem: [System] = linkedSystems[SystemName.position()]

        for spriteComponent in spriteComponentsList:
            entity: Entity = spriteComponent.entityValue
            posComponent: SpriteComponent = positionSystem.componentFor(entity)
            spriteComponent.sprite.position = Point(posComponent.x, posComponent.y)

        return []

    def run(self, linkedSystems: {str, System}) -> [Entity]:
        """Perform the Components processing."""
        spriteComponentsList: [SpriteComponent] = self.m_components.allComponents()

        for spriteComponent in spriteComponentsList:
            sprite: Sprite = spriteComponent.sprite

            if sprite.ready and not self.m_spriteGroup.has(sprite):
                self.m_spriteGroup.add(sprite)

        return []

    def post(self, linkedSystems: {str, System}) -> [Entity]:
        """Do something after processing."""
        self.m_spriteGroup.update()

        AppData.wantAccess()
        self.m_spriteGroup.draw(AppData.window().surface)
        AppData.releaseAccess()
        return []
