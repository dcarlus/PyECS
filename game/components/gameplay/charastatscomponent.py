from ecs.entities import Entity
from ecs.components import Component, ComponentFactory
from ecs.systems import SystemProcessing


class CharacterPropertiesComponent(Component):
    """Component containing the stats of a character."""

    def __init__(self, entity: Entity):
        """Create a new CharaStatComponent instance."""
        super().__init__(entity)
        self.m_name: str = ""

    @property
    def name(self) -> str:
        """Get the name."""
        return self.m_name

    @name.setter
    def name(self, name: str) -> None:
        """Set the name."""
        self.m_name = name


class CharacterPropertiesProcessing(SystemProcessing):
    """System processing of CharacterPropertiesProcessing."""

    def __init__(self, components: ComponentFactory):
        """Create a new CharacterPropertiesProcessing instance."""
        super().__init__(components)