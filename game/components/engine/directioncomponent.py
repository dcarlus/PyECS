from ecs.components import Component
from ecs.entities import Entity
from engine.graphics.direction import Direction


class DirectionComponent(Component):
    """Component for setting the direction of an object in a 2D game. For example, the direction of a character."""

    def __init__(self, entity: Entity) -> None:
        """Create a new PositionComponent instance."""
        super().__init__(entity)
        self.m_direction: Direction = Direction.UP

    @property
    def direction(self) -> Direction:
        """Get the current Direction."""
        return self.m_direction

    @direction.setter
    def direction(self, direction: Direction) -> None:
        """Set the Direction. Only valid values are accepted, otherwise do nothing."""
        if (Direction.contains(direction)):
            self.m_direction = direction