from DemoModule import PositionComponent, PositionProcessing
from EntitiesModule import Entity
from SystemsModule import System
from WorldModule import World

world: World = World()
entity0: Entity = world.createEntity()
entity1: Entity = world.createEntity()

posSystem: System = world.system(PositionComponent, PositionProcessing, "Position")

posCompo0: PositionComponent = posSystem.create(entity0)
posCompo0.x = 2
posCompo0.y = 9
posCompo1: PositionComponent = posSystem.create(entity0)
posCompo1.x = 1
posCompo1.y = 2
posCompo2: PositionComponent = posSystem.create(entity0)
posCompo2.x = 6
posCompo2.y = 4
posCompo3: PositionComponent = posSystem.create(entity1)
posCompo3.x = 3
posCompo3.y = 5
posCompo4: PositionComponent = posSystem.create(entity1)
posCompo4.x = 8
posCompo4.y = 6

print('One run test')
world.run()

print()
print('End setup world data...')
world.debug()

print()
print('Remove:', entity1)
world.delete(entity1)
world.debug()

print()
print('Clear now...')
world.clear()
world.debug()