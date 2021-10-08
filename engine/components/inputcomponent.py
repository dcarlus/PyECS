import pygame
from ecs.components import Component, ComponentFactory
from ecs.entities import Entity
from ecs.systems import SystemProcessing, System
import engine.direction
from engine.geometry import Point
from .spritecomponent import SpriteComponent, Sprite
from .gameplay.charastatscomponent import CharacterPropertiesComponent


class Action:
    """Base class for defining an Action to be performed when an input is activated."""

    def triggered(self) -> None:
        """What is done by the Action."""
        pass


class MoveCharacterAction(Action):
    """Class for moving a Character."""

    def __init__(
        self,
        spriteComponent: SpriteComponent,
        statsComponent: CharacterPropertiesComponent
    ):
        """Create a new MoveCharacterAction instance."""
        super().__init__()
        self.m_spriteComponent: SpriteComponent = spriteComponent
        self.m_statsComponent: statsComponent = statsComponent
        self.m_direction: engine.direction.Direction = engine.direction.Direction.UP
        self.m_moveShift: Point = Point()

    @property
    def direction(self) -> engine.direction.Direction:
        """Get the direction of the move."""
        return self.m_direction

    def setDirection(self, direction: engine.direction.Direction) -> 'MoveCharacterAction':
        """Set the direction of the move."""
        self.m_direction = direction
        return self

    @property
    def shift(self) -> Point:
        """Get the shift of the move."""
        return self.m_moveShift

    def setShift(self, shift: Point) -> 'MoveCharacterAction':
        self.m_moveShift = shift
        return self

    def triggered(self) -> None:
        """What is done by the Action."""
        sprite: Sprite = self.m_spriteComponent.sprite
        shiftCoords: Point = self.m_moveShift.multiplied(self.m_statsComponent.speed)
        sprite.position = sprite.position + shiftCoords
        sprite.changeDirection(self.m_direction)
        sprite.update()


class InputComponent(Component):
    """Component for setting the inputs (keyboard, mouse, controller, ...) applied on an Entity."""

    def __init__(self, entity: Entity) -> None:
        """Create a new PositionComponent instance."""
        super().__init__(entity)
        self.m_keys: {pygame.constants, Action} = {}

    def addKey(self, action: [pygame.constants, Action]) -> None:
        """Add a new input key supported by the current Component."""
        self.m_keys[action[0]] = action[1]

    def removeKey(self, key: pygame.constants) -> None:
        """Remove an input key from the current Component."""
        self.m_keys.discard(key)

    def clear(self):
        """Remove all the input keys from the current Component."""
        self.m_keys.clear()

    def hasKey(self, key: pygame.constants) -> bool:
        """Check if the Component supports an input key."""
        return self.m_keys.__contains__(key)

    def keys(self) -> [pygame.constants]:
        """Get all the available keys."""
        return self.m_keys.keys()

    def trigger(self, key: pygame.constants) -> None:
        """Trigger the Action associated to the key, if found."""
        if self.hasKey(key):
            self.m_keys[key].triggered()


class InputProcessing(SystemProcessing):
    """System processing of InputComponents."""

    def __init__(self, components: ComponentFactory):
        """Create a new InputProcessing instance."""
        super().__init__(components)

    def run(self, linkedSystems: {str, 'System'}, fromIndex: int, toIndex: int) -> None:
        """Perform the Components processing."""
        inputComponentsList: [Component] = self.m_components.allComponents()

        for index in range(fromIndex, toIndex):
            inputComponent: Component = inputComponentsList[index]
            InputProcessing.processKeys(inputComponent)

    @staticmethod
    def processKeys(
        inputComponent: InputComponent
    ) -> bool:
        """Key processing itself with their own logic."""
        pressedKey: [pygame.constants] = pygame.key.get_pressed()
        availableKeys: [pygame.constants] = inputComponent.keys()

        for key in availableKeys:
            if pressedKey[key]:
                inputComponent.trigger(key)
