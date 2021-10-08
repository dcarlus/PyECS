import pygame
from ecs.components import Component, ComponentFactory
from ecs.entities import Entity
from ecs.systems import SystemProcessing, System
from engine.graphics.sprite import Sprite
from game.appdata import AppData

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
        self.m_spriteGroup: pygame.sprite.Group = None

    def setSpriteGroup(self, group: pygame.sprite.Group) -> None:
        """Set the group to which sprites are added."""
        self.m_spriteGroup = group

    def onDelete(self, entity: Entity) -> None:
        """Do something when an entity is removed."""
        if self.m_spriteGroup is not None:
            spriteComponent: SpriteComponent = self.m_components.components(entity)[0]
            self.m_spriteGroup.remove(spriteComponent.sprite)

    def run(self, linkedSystems: {str, 'System'}, fromIndex: int, toIndex: int) -> None:
        """Perform the Components processing."""
        if self.m_spriteGroup is None:
            return

        spriteComponentsList: [SpriteComponent] = self.m_components.allComponents()

        for spriteComponent in spriteComponentsList:
            sprite: Sprite = spriteComponent.sprite

            if sprite.ready and not self.m_spriteGroup.has(sprite):
                AppData.wantAccess()
                self.m_spriteGroup.add(sprite)
                AppData.releaseAccess()
