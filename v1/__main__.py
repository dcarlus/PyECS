from CustomComponentsModule import PositionComponent
from ComponentsModule import ComponentFactory, Component
from EntitiesModule import EntityFactory, Entity

# Tests
print('Create entities')
entityFactory: EntityFactory = EntityFactory()
entity0: Entity = entityFactory.create()
entity1: Entity = entityFactory.create()
entityFactory.debug()
print()

print('Create components')
posCompoFactory: ComponentFactory = ComponentFactory[PositionComponent]()
posCompo0: PositionComponent = posCompoFactory.create(PositionComponent, entity0)
posCompo0.set(5, 2)
posCompo1: PositionComponent = posCompoFactory.create(PositionComponent, entity0)
posCompo1.set(-4, 3)
posCompo2: PositionComponent = posCompoFactory.create(PositionComponent, entity1)
posCompo2.set(-1, 0)
posCompo3: PositionComponent = posCompoFactory.create(PositionComponent, entity0)
posCompo3.set(6, 4)
posCompoFactory.debug()

print()
print('Delete components for the entity0')
posCompoFactory.delete(PositionComponent, entity0)
posCompoFactory.debug()