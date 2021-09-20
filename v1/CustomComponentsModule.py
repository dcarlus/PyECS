from ComponentsModule import Component
from EntitiesModule import Entity


class PositionComponent(Component):
    """Component for setting the 2D position of an object."""

    def __init__(self, entity: Entity) -> None:
        """Create a new PositionComponent instance."""
        super().__init__(entity)
        self.m_x: int = 0
        self.m_y: int = 0

    def set(self, x: int, y: int):
        self.m_x = x
        self.m_y = y

    def setX(self, x: int) -> None:
        """Get the X coordinate of the PositionComponent."""
        self.m_x = x

    def setY(self, y: int) -> None:
        """Get the Y coordinate of the PositionComponent."""
        self.m_y = y

    def x(self) -> int:
        """Get the X coordinate of the PositionComponent."""
        return self.m_x

    def y(self) -> int:
        """Get the Y coordinate of the PositionComponent."""
        return self.m_y

    def __str__(self):
        """Return a string for representing the PositionComponent."""
        return '({}, {})'.format(self.m_x, self.m_y)