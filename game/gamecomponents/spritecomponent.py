import pygame
from ecs.components import Component, ComponentFactory
from ecs.entities import Entity
from ecs.systems import SystemProcessing, System
from game.graphics.sprite import Sprite


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

    def run(self, linkedSystems: [System]) -> None:
        """Perform the Components processing."""
        pass