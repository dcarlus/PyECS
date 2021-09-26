import pygame
from ecs.systems import System
from gamecomponents.positioncomponent import PositionComponent, PositionProcessing
from gamecomponents.inputcomponent import InputComponent, InputProcessing
from gamecomponents.spritecomponent import SpriteComponent, SpriteProcessing
from engine.graphics.sprite import Sprite, Direction
from engine.game import Game
from game.appdata import SystemName, AnimationName


class CrystalShot(Game):
    """Configuration of the game engine for the Crystal Shot game."""

    def __init__(self) -> None:
        """Initialize the Game."""
        super().__init__()
        self.__setupWorld()

    def __setupWorld(self):
        """Setup the game ECS World."""
        self.m_entities.append(self.m_world.createEntity())
        self.m_entities.append(self.m_world.createEntity())

        # Todo: create classes for characters of the game that are an Entity with its Components, registered in the
        #  ECS World.
        self.__createSystems()
        self.__createPositionComponents()
        self.__createInputComponents()
        self.__createSpriteComponents()

    # Todo: this is a temporary code of course!
    def __createSystems(self):
        """Create the different Systems of the Game."""
        posSystem: System = self.m_world.system(SystemName.position(), PositionComponent, PositionProcessing)
        inputSystem: System = self.m_world.system(SystemName.input(), InputComponent, InputProcessing)
        spriteSystem: System = self.m_world.system(SystemName.sprite(), SpriteComponent, SpriteProcessing)
        inputSystem.link(posSystem)
        inputSystem.link(spriteSystem)

    def __createPositionComponents(self):
        """Create the PositionComponents."""
        posSystem: System = self.m_world.system(SystemName.position())
        posCompo0: PositionComponent = posSystem.create(self.m_entities[0])
        posCompo0.x = 2
        posCompo0.y = 9
        posCompo1: PositionComponent = posSystem.create(self.m_entities[1])
        posCompo1.x = 3
        posCompo1.y = 5

    def __createInputComponents(self):
        """Create the InputComponents."""
        inputSystem: System = self.m_world.system(SystemName.input())
        inputCompo0: InputComponent = inputSystem.create(self.m_entities[0])
        inputCompo0.addKey(pygame.K_UP)
        inputCompo0.addKey(pygame.K_DOWN)
        inputCompo0.addKey(pygame.K_LEFT)
        inputCompo0.addKey(pygame.K_RIGHT)
        inputCompo1: InputComponent = inputSystem.create(self.m_entities[1])
        inputCompo1.addKey(pygame.K_q)
        inputCompo1.addKey(pygame.K_d)

    def __createSpriteComponents(self):
        """Create the SpriteComponents."""
        SpriteWidth: int = 64
        SpriteHeight: int = 72
        AmountSprites: int = 9
        WalkAnimationDirections: {Direction, int} = {
            Direction.UP: 9,
            Direction.LEFT: 10,
            Direction.DOWN: 11,
            Direction.RIGHT: 12
        }

        spriteSystem: System = self.m_world.system(SystemName.sprite())
        spriteCompo0: SpriteComponent = spriteSystem.create(self.m_entities[0])
        spriteCompo0.sprite = Sprite('resources/img/sprites/player.png', SpriteWidth, SpriteHeight)
        spriteCompo0.sprite.addAnimation(AnimationName.walk(), WalkAnimationDirections, AmountSprites)
        spriteCompo1: SpriteComponent = spriteSystem.create(self.m_entities[1])
        spriteCompo1.sprite = Sprite('resources/img/sprites/skeleton.png', SpriteWidth, SpriteHeight)
        spriteCompo1.sprite.addAnimation(AnimationName.walk(), WalkAnimationDirections, AmountSprites)