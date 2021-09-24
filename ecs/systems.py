from termcolor import colored
from ecs.components import Component, ComponentFactory, Entity, Generic, Type, TypeVar, TConcreteComponent


class SystemProcessing:
    """Class for processing the components of a System."""

    def __init__(self, components: ComponentFactory):
        """Create a new SystemProcessing instance."""
        self.m_components = components

    def run(self, linkedSystems: []) -> None:
        """Perform the Components processing."""
        return

TConcreteSystemProcessing = TypeVar('TConcreteSystemProcessing', bound=SystemProcessing)

class System(Generic[TConcreteComponent]):
    """Base class for defining a System of the ecs architecture."""

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
        """Create a Component and attach it to the provided Entity."""
        return self.m_components.create(entity)

    def delete(self, entity: Entity) -> None:
        """Delete the component(s) attached to an Entity."""
        self.m_components.delete(entity)

    def link(self, linkedSystem) -> None:
        name: str = linkedSystem.name
        self.m_linkedSystems[name] = linkedSystem

    def unlink(self, system):
        name: str = system.name

        if self.m_linkedSystems.__contains__(name):
            self.m_linkedSystems.pop(name)

    def components(self) -> [Component]:
        """Get all the components managed by the current System."""
        return self.m_components.allComponents()

    def process(self) -> None:
        """Run the Components processing."""
        self.m_processing.run(self.m_linkedSystems)

    @property
    def name(self):
        """Get the name of the System."""
        return self.m_name

    def debug(self) -> None:
        """Debug the System instance."""
        print(colored("[Debug] {}System".format(self.m_memberClass.__name__), 'magenta'))
        self.m_components.debug()