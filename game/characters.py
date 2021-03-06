from ecs.world import World
from ecs.entities import Entity
from ecs.systems import System
from engine.geometry import Point
from engine.components.spritecomponent import SpriteComponent
from engine.components.inputcomponent import InputComponent
from engine.components.renderingcomponent import RenderingComponent
from engine.components.gameplay.charastatscomponent import CharacterPropertiesComponent
from engine.components.gameplay.aicomponent import AIComponent
from game.appdata import SystemName


class Character:
    """Base class for creating a Character."""

    def __init__(self, world: World, name: str):
        """Create a new Character instance."""
        self.m_entity: Entity = world.createEntity()
        self.m_spriteComponent: SpriteComponent = None
        self.m_propertiesComponent: CharacterPropertiesComponent = None
        self.__createComponents(world)
        self.__setProperties(name)

    def __createComponents(self, world: World) -> None:
        """Set up the Entity of the Character."""
        spriteSystem: System = world.system(SystemName.sprite())
        propertiesSystem: System = world.system(SystemName.characterProperties())
        self.m_spriteComponent = spriteSystem.create(self.m_entity)
        self.m_propertiesComponent = propertiesSystem.create(self.m_entity)

    def __setProperties(self, name: str):
        """Set up the Character's properties."""
        self.m_propertiesComponent.name = name

    @property
    def entity(self) -> Entity:
        """Get the Entity of the Character."""
        return self.m_entity

    @property
    def spriteComponent(self) -> SpriteComponent:
        """Get the SpriteComponent of the Character."""
        return self.m_spriteComponent

    @property
    def propertiesComponent(self) -> CharacterPropertiesComponent:
        """Get the CharacterPropertiesComponent of the Character."""
        return self.m_propertiesComponent

    @property
    def position(self) -> Point:
        """Get the position of the Character."""
        if self.m_spriteComponent.sprite.ready:
            return self.m_spriteComponent.sprite.position
        return Point()

    @position.setter
    def position(self, position: Point) -> None:
        """Set the position of the Character."""
        if self.m_spriteComponent.sprite.ready:
            self.m_spriteComponent.sprite.position = position


class Player(Character):
    """Class for a Player that can be moved through inputs (keyboard, controller, ...)."""

    def __init__(self, world: World, name: str = "Player"):
        """Create a new Player instance."""
        super().__init__(world, name)
        self.m_inputComponent: InputComponent = None
        self.__createInputComponent(world)

    def __createInputComponent(self, world) -> None:
        """Create the InputComponent to control the Player."""
        inputSystem: System = world.system(SystemName.input())
        self.m_inputComponent = inputSystem.create(self.m_entity)

    @property
    def inputComponent(self) -> InputComponent:
        """Get the InputComponent of the Player."""
        return self.m_inputComponent


class Bot(Character):
    """Class for a Bot that is controlled by the CPU."""

    def __init__(self, world: World, name: str = "Bot"):
        """Create a new Bot instance."""
        super().__init__(world, name)
        self.m_aiComponent: AIComponent = None
        self.__createAIComponent(world)

    def __createAIComponent(self, world) -> None:
        """Create the AIComponent to control the Bot."""
        aiSystem: System = world.system(SystemName.ai())
        self.m_aiComponent = aiSystem.create(self.m_entity)

    @property
    def aiComponent(self) -> AIComponent:
        """Get the AIComponent of the Bot."""
        return self.m_aiComponent