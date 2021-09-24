from DemoModule import PositionComponent, PositionProcessing, InputComponent, InputProcessing
from EntitiesModule import Entity
from SystemsModule import System
from WorldModule import World
import pygame


pygame.init()

world: World = World()
entity0: Entity = world.createEntity()
entity1: Entity = world.createEntity()

posSystem: System = world.system('Position', PositionComponent, PositionProcessing)
inputSystem: System = world.system('Input', InputComponent, InputProcessing)
inputSystem.link(posSystem)

posCompo0: PositionComponent = posSystem.create(entity0)
posCompo0.x = 2
posCompo0.y = 9
posCompo3: PositionComponent = posSystem.create(entity1)
posCompo3.x = 3
posCompo3.y = 5

inputCompo0: InputComponent = inputSystem.create(entity0)
inputCompo0.addKey(pygame.K_UP)
inputCompo0.addKey(pygame.K_DOWN)
inputCompo0.addKey(pygame.K_LEFT)
inputCompo0.addKey(pygame.K_RIGHT)
inputCompo1: InputComponent = inputSystem.create(entity1)
inputCompo1.addKey(pygame.K_LEFT)
inputCompo1.addKey(pygame.K_RIGHT)

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