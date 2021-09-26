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
        self.m_sprites = pygame.sprite.Group()

    def run(self, linkedSystems: [System]) -> None:
        """Perform the Components processing."""
        spriteComponentsList: [SpriteComponent] = self.m_components.allComponents()

        for spriteComponent in spriteComponentsList:
            sprite: Sprite = spriteComponent.sprite
            pygameSprite = sprite.current

            if pygameSprite is not None and not self.m_sprites.has(sprite):
                self.m_sprites.add(pygameSprite)

    def post(self, linkedSystems: []) -> None:
        """Do something after processing."""
        self.m_sprites.update()

        AppData.wantAccess()
        self.m_sprites.draw(AppData.window().surface)
        AppData.releaseAccess()
