import pygame
from engine.mainwindow import MainWindow
from game.appdata import AppData
from game.crystalshot import CrystalShot

if __name__ == '__main__':
    framerate: int = 60
    csGame: CrystalShot = CrystalShot(framerate)
    AppData.window().framerate = framerate
    AppData.window().showFPS = True
    AppData.window().clearColor = (0, 0, 0)

    running: bool = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                AppData.window().resize(event.size[0], event.size[1])

        AppData.window().clear()
        csGame.world.run()
        AppData.window().update()

    MainWindow.end()
