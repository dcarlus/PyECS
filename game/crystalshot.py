import random

import pygame
from ecs.systems import System
from engine.components.inputcomponent import InputComponent, InputProcessing, MoveCharacterAction
from engine.components.spritecomponent import SpriteComponent, SpriteProcessing
from engine.components.renderingcomponent import RenderingComponent, RenderingProcessing
from engine.components.gameplay.charastatscomponent import CharacterPropertiesComponent, CharacterPropertiesProcessing
from engine.components.gameplay.aicomponent import AIComponent, AIProcessing
from engine.graphics.sprite import Sprite, Direction
from engine.geometry import Point
from engine.game import Game
from game.appdata import SystemName, AnimationName
from characters import Player, Bot


class CrystalShot(Game):
    """Configuration of the game engine for the Crystal Shot game."""

    def __init__(self, framerate: int) -> None:
        """Initialize the Game."""
        super().__init__()
        pygame.key.set_repeat(int((1./framerate) * 1000))
        self.__setupWorld()

    def __setupWorld(self) -> None:
        """Setup the game ECS World."""
        self.__createSystems()
        self.__generateBots(128)
        # self.__generatePlayer()

    def __generateBots(self, count: int) -> None:
        """Generate the Bots of the Game."""
        for index in range(count):
            newBot: Bot = Bot(self.m_world)
            self.m_entities.append(newBot.entity)

            SpriteWidth: int = 64
            SpriteHeight: int = 64
            AmountSprites: int = 9
            WalkAnimationDirections: {Direction, int} = {
                Direction.UP: 8,
                Direction.LEFT: 9,
                Direction.DOWN: 10,
                Direction.RIGHT: 11
            }
            newBot.spriteComponent.sprite = Sprite('resources/img/sprites/skeleton.png', SpriteWidth, SpriteHeight)
            newBot.spriteComponent.sprite.addAnimation(AnimationName.walk(), WalkAnimationDirections, AmountSprites)
            newBot.spriteComponent.sprite.changeAnimation(AnimationName.walk())

            newBot.propertiesComponent.speed = random.randint(1, 2)
            newBot.propertiesComponent.life = random.randint(3999, 9999)
            newBot.propertiesComponent.attack = random.randint(2, 20)
            newBot.position = Point(random.randint(0, 800), random.randint(0, 600))

    def __generatePlayer(self) -> None:
        """Generate the Player of the Game."""
        player: Player = Player(self.m_world, "Anna")
        self.m_entities.append(player.entity)

        WalkAnimationDirections: {Direction, int} = {
            Direction.UP: 8,
            Direction.LEFT: 9,
            Direction.DOWN: 10,
            Direction.RIGHT: 11
        }

        SpriteWidth: int = 64
        SpriteHeight: int = 64
        AmountSprites: int = 9
        player.spriteComponent.sprite = Sprite('resources/img/sprites/player.png', SpriteWidth, SpriteHeight)
        player.spriteComponent.sprite.addAnimation(AnimationName.walk(), WalkAnimationDirections, AmountSprites)
        player.spriteComponent.sprite.changeAnimation(AnimationName.walk())

        player.propertiesComponent.speed = 2
        player.position = Point(2, 9)

        moveUpAction = MoveCharacterAction(
            player.spriteComponent,
            player.propertiesComponent
        ) \
            .setDirection(Direction.UP) \
            .setShift(Point(0, -1))
        moveDownAction = MoveCharacterAction(
            player.spriteComponent,
            player.propertiesComponent
        ) \
            .setDirection(Direction.DOWN) \
            .setShift(Point(0, 1))
        moveLeftAction = MoveCharacterAction(
            player.spriteComponent,
            player.propertiesComponent
        ) \
            .setDirection(Direction.LEFT) \
            .setShift(Point(-1, 0))
        moveRightAction = MoveCharacterAction(
            player.spriteComponent,
            player.propertiesComponent
        ) \
            .setDirection(Direction.RIGHT) \
            .setShift(Point(1, 0))

        player.inputComponent.addKey([pygame.K_UP, moveUpAction])
        player.inputComponent.addKey([pygame.K_DOWN, moveDownAction])
        player.inputComponent.addKey([pygame.K_LEFT, moveLeftAction])
        player.inputComponent.addKey([pygame.K_RIGHT, moveRightAction])

    def __createSystems(self) -> None:
        """Create the different Systems of the Game."""
        spriteGroup: pygame.sprite.Group = pygame.sprite.Group()

        inputSystem: System = self.m_world.system(SystemName.input(), InputComponent, InputProcessing)
        spriteSystem: System = self.m_world.system(SystemName.sprite(), SpriteComponent, SpriteProcessing)
        spriteSystem.setProcessingData(spriteGroup, 'setSpriteGroup')

        charPropSystem: System = self.m_world.system(
            SystemName.characterProperties(),
            CharacterPropertiesComponent,
            CharacterPropertiesProcessing
        )

        aiSystem: System = self.m_world.system(SystemName.ai(), AIComponent, AIProcessing)
        aiSystem.link(spriteSystem)
        aiSystem.link(charPropSystem)

        renderingSystem: System = self.m_world.system(SystemName.rendering(), RenderingComponent, RenderingProcessing)
        renderingSystem.setProcessingData(spriteGroup, 'setSpriteGroup')