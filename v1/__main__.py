from CustomComponentsModule import PositionComponent
from EntitiesModule import Entity
from WorldModule import World

world: World = World()
entity0: Entity = world.createEntity()
entity1: Entity = world.createEntity()

posCompo0: PositionComponent = world.createComponent(PositionComponent, entity0)
posCompo0.x = 2
posCompo0.y = 9
posCompo1: PositionComponent = world.createComponent(PositionComponent, entity0)
posCompo1.x = 1
posCompo1.y = 2
posCompo2: PositionComponent = world.createComponent(PositionComponent, entity0)
posCompo2.x = 6
posCompo2.y = 4
posCompo3: PositionComponent = world.createComponent(PositionComponent, entity1)
posCompo3.x = 3
posCompo3.y = 5

world.debug()
print()
world.delete(entity0)
world.debug()