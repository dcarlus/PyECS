import pygame
from ecs.components import Component, ComponentFactory
from ecs.entities import Entity
from ecs.systems import SystemProcessing, System
from game.appdata import SystemName
from engine.graphics.direction import Direction
from engine.graphics.geometry import Point
from .positioncomponent import PositionComponent
from .spritecomponent import SpriteComponent


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
        self.m_frameCounter: int = 0

    def run(self, linkedSystems: [System]) -> None:
        """Perform the Components processing."""
        self.m_frameCounter = self.m_frameCounter + 1
        inputComponentsList: [Component] = self.m_components.allComponents()
        positionSystem: System = linkedSystems[SystemName.position()]
        spriteSystem: System = linkedSystems[SystemName.sprite()]

        for inputComponent in inputComponentsList:
            entity: Entity = inputComponent.entity

            # Look for the position and sprite components attached to the same Entity (only one is allowed per Entity).
            positionComponent: PositionComponent = positionSystem.componentFor(entity)
            spriteComponent: SpriteComponent = spriteSystem.componentFor(entity)

            if positionComponent is None or spriteComponent is None:
                continue

            needAnimation: bool = InputProcessing.processKeys(inputComponent, positionComponent, spriteComponent)

            if needAnimation and (self.m_frameCounter % 10) == 0:
                spriteComponent.sprite.nextSprite()

    @staticmethod
    def processKeys(
        inputComponent: InputComponent,
        positionComponent: PositionComponent,
        spriteComponent: SpriteComponent
    ) -> bool:
        """Key processing itself with their own logic."""
        # Todo: create a CharacterProperties component?
        characterSpeed: int = 2

        needAnimation: bool = False
        pressedKey: pygame.constants = pygame.key.get_pressed()
        spriteDirection: Direction = None

        if pressedKey[pygame.K_UP] and inputComponent.hasKey(pygame.K_UP):
            positionComponent.y = positionComponent.y - characterSpeed
            spriteDirection = Direction.UP

        if pressedKey[pygame.K_DOWN] and inputComponent.hasKey(pygame.K_DOWN):
            positionComponent.y = positionComponent.y + characterSpeed
            spriteDirection = Direction.DOWN

        if pressedKey[pygame.K_LEFT] and inputComponent.hasKey(pygame.K_LEFT):
            positionComponent.x = positionComponent.x - characterSpeed
            spriteDirection = Direction.LEFT

        if pressedKey[pygame.K_RIGHT] and inputComponent.hasKey(pygame.K_RIGHT):
            positionComponent.x = positionComponent.x + characterSpeed
            spriteDirection = Direction.RIGHT

        if spriteDirection is not None:
            needAnimation = True
            spriteComponent.sprite.changeDirection(spriteDirection)
            spriteComponent.sprite.position = Point(positionComponent.x, positionComponent.y)
            spriteComponent.sprite.update()

        return needAnimation
