from EntitiesModule import *
from ComponentsModule import *
from CustomComponentsModule import *


class World:

    def __init__(self):
        """Create a new World instance."""
        self.m_entities: EntityFactory = EntityFactory()
        self.m_components = {}

    def createEntity(self) -> Entity:
        """Create an Entity instance."""
        return self.m_entities.create()

    def createComponent(self, componentClass, entity: Entity) -> TConcreteComponent:
        """Create a Component for the given class."""
        if not self.m_components.__contains__(componentClass):
            self.m_components[componentClass] = ComponentFactory(componentClass)
        return self.m_components[componentClass].create(entity)

    def delete(self, entity: Entity) -> None:
        """Delete an Entity and all its attached Components."""
        for key in self.m_components:
            self.m_components[key].delete(entity)
        self.m_entities.delete(entity)

    def debug(self):
        """Debug the World instance."""
        self.m_entities.debug()
        for key in self.m_components:
            self.m_components[key].debug()