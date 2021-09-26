import pygame
from ecs.entities import Entity
from ecs.world import World


class Game:
    """Configuration of the game engine."""

    def __init__(self) -> None:
        """Initialize the Game."""
        pygame.init()
        self.m_entities: [Entity] = []
        self.m_world: World = World()

    @property
    def world(self) -> World:
        """Get the game ECS World."""
        return self.m_world