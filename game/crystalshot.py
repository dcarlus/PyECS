import pygame
from ecs.systems import System
from game.components.engine.positioncomponent import PositionComponent, PositionProcessing
from game.components.engine.inputcomponent import InputComponent, InputProcessing
from game.components.engine.spritecomponent import SpriteComponent, SpriteProcessing
from game.components.gameplay.charastatscomponent import CharacterPropertiesComponent, CharacterPropertiesProcessing
from engine.graphics.sprite import Sprite, Direction
from engine.game import Game
from game.appdata import SystemName, AnimationName
from characters import Player


class CrystalShot(Game):
    """Configuration of the game engine for the Crystal Shot game."""

    def __init__(self, framerate: int) -> None:
        """Initialize the Game."""
        super().__init__()
        pygame.key.set_repeat(int((1./framerate) * 1000))
        self.__setupWorld()

    def __setupWorld(self):
        """Setup the game ECS World."""
        self.__createSystems()
        self.__generateCharacters()

    def __generateCharacters(self):
        """Generate the Characters of the Game."""
        player: Player = Player(self.m_world, "Anna")
        self.m_entities.append(player.entity)

        player.positionSystem.x = 2
        player.positionSystem.y = 9

        SpriteWidth: int = 64
        SpriteHeight: int = 64
        AmountSprites: int = 9
        WalkAnimationDirections: {Direction, int} = {
            Direction.UP: 8,
            Direction.LEFT: 9,
            Direction.DOWN: 10,
            Direction.RIGHT: 11
        }
        player.spriteComponent.sprite = Sprite('resources/img/sprites/player.png', SpriteWidth, SpriteHeight)
        player.spriteComponent.sprite.addAnimation(AnimationName.walk(), WalkAnimationDirections, AmountSprites)
        player.spriteComponent.sprite.changeAnimation(AnimationName.walk())

        player.inputComponent.addKey(pygame.K_UP)
        player.inputComponent.addKey(pygame.K_DOWN)
        player.inputComponent.addKey(pygame.K_LEFT)
        player.inputComponent.addKey(pygame.K_RIGHT)

    # Todo: this is a temporary code of course!
    def __createSystems(self):
        """Create the different Systems of the Game."""
        posSystem: System = self.m_world.system(SystemName.position(), PositionComponent, PositionProcessing)
        inputSystem: System = self.m_world.system(SystemName.input(), InputComponent, InputProcessing)
        spriteSystem: System = self.m_world.system(SystemName.sprite(), SpriteComponent, SpriteProcessing)
        inputSystem.link(posSystem)
        inputSystem.link(spriteSystem)
        charPropSystem: System = self.m_world.system(
            SystemName.characterProperties(),
            CharacterPropertiesComponent,
            CharacterPropertiesProcessing
        )