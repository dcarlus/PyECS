from EntitiesModule import Entity, EntityFactory
from SystemsModule import System, Type, TConcreteComponent, TConcreteSystemProcessing


class World:
    """Entry class for using the ECS instances. Handles interactions between these instances as automatic data
    suppression. For example, it removes all the components attached to an entity when this one is deleted."""

    def __init__(self):
        """Create a new World instance."""
        self.m_entities: EntityFactory = EntityFactory()
        self.m_entityList = []
        self.m_systems = {}

    def __del__(self):
        """Clear data on World destruction."""
        self.clear()

    def clear(self):
        """Clear all data of the current World."""
        while len(self.m_entityList) > 0:
            self.delete(self.m_entityList[0])

    def createEntity(self) -> Entity:
        """Create an Entity instance."""
        newEntity: Entity = self.m_entities.create()
        self.m_entityList.append(newEntity)
        return newEntity

    def system(
        self,
        name: str,
        componentClass: Type[TConcreteComponent],
        processingClass: Type[TConcreteSystemProcessing]
    ) -> System:
        """Get a System by its name."""
        if not self.m_systems.__contains__(name):
            self.m_systems[name] = System(name, componentClass, processingClass)
        return self.m_systems[name]

    def delete(self, entity: Entity) -> None:
        """Delete an Entity and all its attached Components."""
        for name in self.m_systems:
            self.m_systems[name].delete(entity)
        self.m_entities.delete(entity)

        try:
            self.m_entityList.remove(entity)
        except:
            pass

    def run(self):
        """Run all the registered Systems in the World."""
        for name in self.m_systems:
            self.m_systems[name].process()

    def debug(self) -> None:
        """Debug the World instance."""
        self.m_entities.debug()
        for name in self.m_systems:
            self.m_systems[name].debug()