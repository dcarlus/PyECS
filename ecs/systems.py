from termcolor import colored
from typing import Any
from ecs.components import Component, ComponentQuantity, ComponentFactory, Entity, Generic, Type, TypeVar, TConcreteComponent


class SystemProcessing:
    """Class for processing the components of a System."""

    def __init__(self, components: ComponentFactory):
        """Create a new SystemProcessing instance."""
        self.m_components = components

    def setData(self, data: Any, setterName: str) -> None:
        """Set data by calling the setter method by its name."""
        setter: 'function' = getattr(self, setterName)
        setter(data)

    def onDelete(self, entity: Entity) -> None:
        """Do something when an entity is removed."""
        return

    # def pre(self, linkedSystems: {str, 'System'}) -> [Entity]:
    #     """Prepare work before run. Returns a list of Entity to be removed by the World."""
    #     return []

    def run(self, linkedSystems: {str, 'System'}) -> [Entity]:
        """Perform the Components processing. Returns a list of Entity to be removed by the World."""
        return []

    # def post(self, linkedSystems: {str, 'System'}) -> [Entity]:
    #     """Do something after processing. Returns a list of Entity to be removed by the World."""
    #     return []

TConcreteSystemProcessing = TypeVar('TConcreteSystemProcessing', bound=SystemProcessing)

class System(Generic[TConcreteComponent]):
    """Base class for defining a System of the ECS architecture."""

    def __init__(
        self,
        name: str,
        componentClass: Type[TConcreteComponent],
        processingClass: Type[TConcreteComponent]
    ):
        """Create a new System instance."""
        self.m_name = name
        self.m_memberClass = componentClass
        self.m_linkedSystems: {str, System} = {}
        self.m_components = ComponentFactory(componentClass)
        self.m_processing = processingClass(self.m_components)

    def create(self, entity: Entity) -> TConcreteComponent:
        """If the Entity has no Component of the wanted type, it creates a new Component and attach it to the provided
        Entity.
        In the case where the Entity already has a Component of the wanted type and cannot have more than one Component
        of this type, it returns the previously created Component attached to that Entity."""
        quantity: ComponentQuantity = self.m_memberClass.quantity()

        if quantity is ComponentQuantity.ONE:
            listComponents: [Component] = self.m_components.components(entity)

            if len(listComponents) > 0:
                return listComponents[0]

        return self.m_components.create(entity)

    def delete(self, entity: Entity) -> None:
        """Delete the component(s) attached to an Entity."""
        self.m_processing.onDelete(entity)
        self.m_components.delete(entity)

    def link(self, linkedSystem) -> None:
        name: str = linkedSystem.name
        self.m_linkedSystems[name] = linkedSystem

    def unlink(self, system):
        name: str = system.name

        if self.m_linkedSystems.__contains__(name):
            self.m_linkedSystems.pop(name)

    def components(self) -> [Component]:
        """Get all the Components managed by the current System."""
        return self.m_components.allComponents()

    def componentFor(self, entity: Entity) -> Component:
        """Get the first Component found for the given entity."""
        try:
            return next(c for c in self.components() if c.entityValue == entity)
        except:
            return None

    def allComponentsFor(self, entity: Entity) -> [Component]:
        """Get the Components found for the given entity."""
        foundComponents: [Component] = []
        listComponents: [Component] = self.m_components.allComponents()

        for component in listComponents:
            if component.entityValue == entity:
                foundComponents.append(component)

        return foundComponents

    def process(self) -> [Entity]:
        """Run the Components processing. Returns a list of Entity to be removed by the World."""
        return self.m_processing.run(self.m_linkedSystems)

    def setProcessingData(self, data: Any, setterName: str) -> None:
        """Set data to the system processing."""
        self.m_processing.setData(data, setterName)

    @property
    def name(self):
        """Get the name of the System."""
        return self.m_name

    def debug(self) -> None:
        """Debug the System instance."""
        print(colored("[Debug] {}System".format(self.m_memberClass.__name__), 'magenta'))
        self.m_components.debug()