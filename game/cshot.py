import pygame
from ecs.entities import Entity
from ecs.systems import System
from ecs.world import World
import gamecomponents.componentnaming as names
from gamecomponents.positioncomponent import PositionComponent, PositionProcessing
from gamecomponents.inputcomponent import InputComponent, InputProcessing
from gamecomponents.spritecomponent import SpriteComponent, SpriteProcessing
from engine.graphics.sprite import Sprite


def getWorld() -> World:
    """Setup the game ECS World."""
    world: World = World()
    entity0: Entity = world.createEntity()
    entity1: Entity = world.createEntity()

    posSystem: System = world.system(names.PositionSystemName, PositionComponent, PositionProcessing)
    inputSystem: System = world.system(names.InputSystemName, InputComponent, InputProcessing)
    spriteSystem: System = world.system(names.SpriteSystemName, SpriteComponent, SpriteProcessing)
    inputSystem.link(posSystem)
    inputSystem.link(spriteSystem)

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

    spriteCompo0: SpriteComponent = spriteSystem.create(entity0)
    spriteCompo0.sprite = Sprite('resources/img/sprites/player.png', 64, 72)
    spriteCompo1: SpriteComponent = spriteSystem.create(entity1)
    spriteCompo1.sprite = Sprite('resources/img/sprites/skeleton.png', 64, 72)

    return world