from ecs.world import World
from ecs.entities import Entity
from ecs.systems import System
from game.components.engine.positioncomponent import PositionComponent, Point
from game.components.engine.spritecomponent import SpriteComponent
from game.components.engine.inputcomponent import InputComponent
from game.components.gameplay.charastatscomponent import CharacterPropertiesComponent
from game.appdata import SystemName


class Character:
    """Base class for creating a Character."""

    def __init__(self, world: World, name: str):
        """Create a new Character instance."""
        self.m_entity: Entity = world.createEntity()
        self.m_positionComponent: PositionComponent = None
        self.m_spriteComponent: SpriteComponent = None
        self.m_propertiesComponent: CharacterPropertiesComponent = None
        self.__createComponents(world)
        self.__setProperties(name)

    def __createComponents(self, world: World) -> None:
        """Set up the Entity of the Character."""
        positionSystem: System = world.system(SystemName.position())
        spriteSystem: System = world.system(SystemName.sprite())
        propertiesSystem: System = world.system(SystemName.characterProperties())
        self.m_positionComponent = positionSystem.create(self.m_entity)
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
    def positionSystem(self) -> PositionComponent:
        """Get the PositionComponent of the Character."""
        return self.m_positionComponent

    @property
    def spriteComponent(self) -> SpriteComponent:
        """Get the SpriteComponent of the Character."""
        return self.m_spriteComponent

    @property
    def propertiesComponent(self) -> CharacterPropertiesComponent:
        """Get the CharacterPropertiesComponent of the Character."""
        return self.m_propertiesComponent


class Player(Character):
    """Class for a Player that can be moved through inputs (keyboard, controller, ...)"""

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
        """Get the InpurComponent of the Player."""
        return self.m_inputComponent