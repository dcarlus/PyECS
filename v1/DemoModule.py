from ComponentsModule import Component, ComponentFactory
from EntitiesModule import Entity
from SystemsModule import SystemProcessing


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


class PositionProcessing(SystemProcessing):
    """System processing of PositionComponents."""

    def __init__(self, components: ComponentFactory):
        super().__init__(components)

    def run(self) -> None:
        """Perform the Components processing."""
        componentsList: [Component] = self.m_components.allComponents()

        for component in componentsList:
            if not component.hasValidEntity():
                continue

            print("Run process on position ({},{}) for {}".format(
                    component.x,
                    component.y,
                    component.entity
                )
            )