# Module containing user defined components and system processing.
# Here some demonstration components and system processing for a 2D video game using pygame.
from ecs.components import Component, ComponentQuantity, ComponentFactory
from ecs.entities import Entity
from ecs.systems import SystemProcessing, System
import pygame
import cshot


# POSITION
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
        """Create a new PositionProcessing instance."""
        super().__init__(components)


# INPUTS
class InputComponent(Component):
    """Component for setting the inputs (keyboard, mouse, controller, ...) applied on an Entity."""

    def __init__(self, entity: Entity) -> None:
        """Create a new PositionComponent instance."""
        super().__init__(entity)
        self.m_keys: {pygame.constants} = set()

    def addKey(self, key: pygame.constants) -> None:
        """Add a new input key supported by the current Component."""
        self.m_keys.add(key)

    def removeKey(self, key: pygame.constants) -> None:
        """Remove an input key from the current Component."""
        self.m_keys.discard(key)

    def clear(self):
        """Remove all the input keys from the current Component."""
        self.m_keys.clear()

    def hasKey(self, key: pygame.constants) -> bool:
        """Check if the Component supports an input key."""
        return self.m_keys.__contains__(key)

    def __str__(self):
        """Return a string for representing the InputComponent."""
        output: str = "{ "

        for key in self.m_keys:
            output += pygame.key.name(key) + " "

        output += "}"
        return output


class InputProcessing(SystemProcessing):
    """System processing of InputComponents."""

    def __init__(self, components: ComponentFactory):
        """Create a new InputProcessing instance."""
        super().__init__(components)

    def run(self, linkedSystems: [System]) -> None:
        """Perform the Components processing."""
        inputComponentsList: [Component] = self.m_components.allComponents()

        positionSystemName: str = next(s for s in linkedSystems if linkedSystems[s].name == cshot.PositionSystemName)
        positionComponentsList: [Component] = linkedSystems[positionSystemName].components()

        for inputComponent in inputComponentsList:
            entity: Entity = inputComponent.entity

            # Look for the position component attached to the same Entity.
            positionComponent: Component = next(c for c in positionComponentsList if c.entity == entity)

            if positionComponent is None:
                continue

            pressedKey: pygame.constants = pygame.key.get_pressed()

            # Logic with the keys.
            if pressedKey[pygame.K_UP] and inputComponent.hasKey(pygame.K_UP):
                positionComponent.x = positionComponent.x - 1
                print("Up pressed: {}".format(positionComponent))

            if pressedKey[pygame.K_DOWN] and inputComponent.hasKey(pygame.K_DOWN):
                positionComponent.x = positionComponent.x + 1
                print("Down pressed: {}".format(positionComponent))

            if pressedKey[pygame.K_LEFT] and inputComponent.hasKey(pygame.K_LEFT):
                positionComponent.y = positionComponent.y - 1
                print("Left pressed: {}".format(positionComponent))

            if pressedKey[pygame.K_RIGHT] and inputComponent.hasKey(pygame.K_RIGHT):
                positionComponent.y = positionComponent.y + 1
                print("Right pressed: {}".format(positionComponent))