from ecs.entities import Entity
from ecs.components import Component, ComponentFactory
from ecs.systems import SystemProcessing


class CharacterPropertiesComponent(Component):
    """Component containing the stats of a character."""

    def __init__(self, entity: Entity):
        """Create a new CharaStatComponent instance."""
        super().__init__(entity)
        self.m_name: str = ""
        self.m_life: int = 1
        self.m_attack: int = 1
        self.m_speed: int = 1

    @property
    def name(self) -> str:
        """Get the name."""
        return self.m_name

    @name.setter
    def name(self, name: str) -> None:
        """Set the name."""
        self.m_name = name

    @property
    def life(self) -> int:
        """Get the life."""
        return self.m_life

    @life.setter
    def life(self, life: int) -> None:
        """Set the life."""
        self.m_life = life

    @property
    def attack(self) -> int:
        """Get the attack."""
        return self.m_attack

    @life.setter
    def attack(self, attack: int) -> None:
        """Set the attack."""
        self.m_attack = attack

    @property
    def speed(self) -> int:
        """Get the speed."""
        return self.m_speed

    @speed.setter
    def speed(self, speed: int) -> None:
        """Set the speed."""
        self.m_speed = speed


class CharacterPropertiesProcessing(SystemProcessing):
    """System processing of CharacterPropertiesProcessing."""

    def __init__(self, components: ComponentFactory):
        """Create a new CharacterPropertiesProcessing instance."""
        super().__init__(components)

    def run(self, linkedSystems: {str, 'System'}, fromIndex: int, toIndex: int) -> [Entity]:
        """Perform the CharacterPropertiesProcessing processing."""
        return self.filterEntities(fromIndex, toIndex)

    def filterEntities(self,  fromIndex: int, toIndex: int) -> [Entity]:
        """Filter Entities of dead Characters."""
        charPropsComponentsList: [CharacterPropertiesComponent] = self.m_components.allComponents()
        entitiesToRemove: [Entity] = []

        for index in range(fromIndex, toIndex):
            component: Component = charPropsComponentsList[index]
            if component.life == 0:
                entitiesToRemove.append(component.entity)

        return entitiesToRemove
