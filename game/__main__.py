import pygame
import cshot
from mainwindow import MainWindow
from ecs.world import World


window: MainWindow = MainWindow(800, 600, 'Crystal Shot')
window.framerate = 75
world: World = cshot.get_world()

running: bool = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            window.resize(event.size[0], event.size[1])

        world.run()
        window.update()

MainWindow.end()