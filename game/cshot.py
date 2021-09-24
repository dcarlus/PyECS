import pygame
from gamecomponents import PositionComponent, PositionProcessing, InputComponent, InputProcessing
from ecs.entities import Entity
from ecs.systems import System
from ecs.world import World


PositionSystemName: str = 'Position'
InputSystemName: str = 'Input'


def get_world() -> World:
    """Setup the game ECS World."""
    world: World = World()
    entity0: Entity = world.createEntity()
    entity1: Entity = world.createEntity()

    posSystem: System = world.system(PositionSystemName, PositionComponent, PositionProcessing)
    inputSystem: System = world.system(InputSystemName, InputComponent, InputProcessing)
    inputSystem.link(posSystem)

    posCompo0: PositionComponent = posSystem.create(entity0)
    posCompo0.x = 2
    posCompo0.y = 9
    posCompo1: PositionComponent = posSystem.create(entity1)
    posCompo1.x = 3
    posCompo1.y = 5

    inputCompo0: InputComponent = inputSystem.create(entity0)
    inputCompo0.addKey(pygame.K_UP)
    inputCompo0.addKey(pygame.K_DOWN)
    inputCompo0.addKey(pygame.K_LEFT)
    inputCompo0.addKey(pygame.K_RIGHT)
    inputCompo1: InputComponent = inputSystem.create(entity1)
    inputCompo1.addKey(pygame.K_q)
    inputCompo1.addKey(pygame.K_d)

    return world