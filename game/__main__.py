import pygame
from engine.mainwindow import MainWindow
from game.appdata import AppData
from game.crystalshot import CrystalShot

csGame: CrystalShot = CrystalShot()
running: bool = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            AppData.window().resize(event.size[0], event.size[1])

        csGame.world.run()
        AppData.window().update()

MainWindow.end()