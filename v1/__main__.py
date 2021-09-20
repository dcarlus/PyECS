from CustomComponentsModule import PositionComponent
from ComponentsModule import ComponentFactory, Component
from EntitiesModule import EntityFactory, Entity
from WorldModule import World

world: World = World()
entity0: Entity = world.createEntity()
entity1: Entity = world.createEntity()

posCompo0: PositionComponent = world.createComponent(PositionComponent, entity0)
posCompo0.set(2, 6)
posCompo1: PositionComponent = world.createComponent(PositionComponent, entity0)
posCompo1.set(9, 3)
posCompo2: PositionComponent = world.createComponent(PositionComponent, entity0)
posCompo2.set(1, 8)
posCompo3: PositionComponent = world.createComponent(PositionComponent, entity1)
posCompo3.set(7, 2)

world.debug()
print()
world.delete(entity0)
world.debug()