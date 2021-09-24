import pygame
import cshot
from mainwindow import MainWindow
from ecs.world import World


window: MainWindow = MainWindow(800, 600, 'Crystal Shot')
world: World = cshot.get_world()

running: bool = True
clock: pygame.time = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            window.resize(event.size[0], event.size[1])

        world.run()
        window.draw()
        clock.tick(60)

MainWindow.end()