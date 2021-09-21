from ComponentsModule import Component
from EntitiesModule import Entity


class PositionComponent(Component):
    """Component for setting the 2D position of an object."""

    def __init__(self, entity: Entity) -> None:
        """Create a new PositionComponent instance."""
        super().__init__(entity)
        self.m_x: int = 0
        self.m_y: int = 0

    @property
    def x(self) -> int:
        """Get the X coordinate of the PositionComponent."""
        return self.m_x

    @property
    def y(self) -> int:
        """Get the Y coordinate of the PositionComponent."""
        return self.m_y

    @x.setter
    def x(self, x: int) -> None:
        """Get the X coordinate of the PositionComponent."""
        self.m_x = x

    @y.setter
    def y(self, y: int) -> None:
        """Get the Y coordinate of the PositionComponent."""
        self.m_y = y

    def __str__(self):
        """Return a string for representing the PositionComponent."""
        return '({}, {})'.format(self.m_x, self.m_y)