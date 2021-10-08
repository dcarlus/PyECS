import pygame
from ecs.components import Component, ComponentFactory
from ecs.entities import Entity
from ecs.systems import SystemProcessing, System
from game.appdata import AppData


class RenderingComponent(Component):
    """Component for performing the rendering."""

    def __init__(self, entity: Entity) -> None:
        super().__init__(entity)


class RenderingProcessing(SystemProcessing):
    """System processing of RenderingComponent."""

    def __init__(self, components: ComponentFactory):
        """Create a new RenderingProcessing instance."""
        super().__init__(components)
        self.m_spriteGroup: pygame.sprite.Group = None

    def setSpriteGroup(self, group: pygame.sprite.Group) -> None:
        """Set the group to which sprites are added."""
        self.m_spriteGroup = group

    def run(self, linkedSystems: {str, 'System'}, fromIndex: int, toIndex: int) -> None:
        """Perform the Components processing."""
        self.m_spriteGroup.update()
        self.m_spriteGroup.draw(AppData.window().surface)