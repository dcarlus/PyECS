import copy

from ecs.components import Component, ComponentFactory
from ecs.entities import Entity
from ecs.systems import SystemProcessing
from engine.graphics.geometry import Point


class PositionComponent(Component):
    """Component for setting the 2D position of an object."""

    def __init__(self, entity: Entity) -> None:
        """Create a new PositionComponent instance."""
        super().__init__(entity)
        self.m_position: Point = Point()

    @property
    def x(self) -> int:
        """Get the X coordinate of the PositionComponent."""
        return self.m_position.x

    @property
    def y(self) -> int:
        """Get the Y coordinate of the PositionComponent."""
        return self.m_position.y

    @x.setter
    def x(self, x: int) -> None:
        """Get the X coordinate of the PositionComponent."""
        self.m_position.x = x

    @y.setter
    def y(self, y: int) -> None:
        """Get the Y coordinate of the PositionComponent."""
        self.m_position.y = y

    @property
    def position(self) -> Point:
        copied: Point = copy.deepcopy(self.m_position)
        return copied

    def __str__(self):
        """Return a string for representing the PositionComponent."""
        return str(self.m_position)


class PositionProcessing(SystemProcessing):
    """System processing of PositionComponents."""

    def __init__(self, components: ComponentFactory):
        """Create a new PositionProcessing instance."""
        super().__init__(components)