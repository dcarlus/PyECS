from ComponentsModule import ComponentFactory, Entity, Generic, Type, TypeVar, TConcreteComponent
from termcolor import colored


class SystemProcessing:
    """Class for processing the components of a System."""

    def __init__(self, components: ComponentFactory):
        """Create a new SystemProcessing instance."""
        self.m_components = components

    def run(self) -> None:
        """Perform the Components processing."""
        return

TConcreteSystemProcessing = TypeVar('TConcreteSystemProcessing', bound=SystemProcessing)

class System(Generic[TConcreteComponent]):
    """Base class for defining a System of the ECS architecture."""

    def __init__(
        self,
        componentClass: Type[TConcreteComponent],
        processingClass: Type[TConcreteComponent]
    ):
        """Create a new System instance."""
        self.m_memberClass = componentClass
        self.m_components = ComponentFactory(componentClass)
        self.m_processing = processingClass(self.m_components)

    def create(self, entity: Entity) -> TConcreteComponent:
        """Create a Component and attach it to the provided Entity."""
        return self.m_components.create(entity)

    def delete(self, entity: Entity) -> None:
        """Delete the component(s) attached to an Entity."""
        self.m_components.delete(entity)

    def process(self) -> None:
        """Run the Components processing."""
        self.m_processing.run()

    def debug(self) -> None:
        """Debug the System instance."""
        print(colored("[Debug] {}System".format(self.m_memberClass.__name__), 'magenta'))
        self.m_components.debug()