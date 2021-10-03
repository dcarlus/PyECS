import pygame

class MainWindow:
    """Main window of the game."""

    def __init__(
        self,
        width: int = 800,
        height: int = 600,
        caption: str = "New window",
        iconPath: str = ''
    ):
        """Create a new MainWindow instance."""
        pygame.init()
        self.m_surface = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.set_caption(caption)
        self.m_framerate: int = 60
        self.m_clock: pygame.time = pygame.time.Clock()
        self.m_clearColor: (int, int, int) = (0, 0, 0)
        self.m_showFPS: bool = False
        self.m_fpsFont = pygame.font.SysFont('Arial', 18)

        if len(iconPath) > 0:
            icon: pygame.Surface = pygame.image.load(iconPath)
            pygame.display.set_icon(icon)

    def clear(self) -> None:
        """Clear the content of the MainWindow with the clear color."""
        self.m_surface.fill(self.m_clearColor)

    @property
    def clearColor(self) -> (int, int, int):
        """Get the clear color (r, g, b) when erasing the content of the MaiWindow."""
        return self.m_clearColor

    @clearColor.setter
    def clearColor(self, color: (int, int, int)) -> None:
        """Set the clear color (r, g, b) when erasing the content of the MaiWindow."""
        self.m_clearColor = color

    @staticmethod
    def end() -> None:
        """End the game application."""
        print('Quit {}'.format(pygame.display.get_caption()[0]))
        pygame.quit()

    @property
    def framerate(self) -> int:
        """Get the framerate of the application."""
        return self.m_framerate

    @framerate.setter
    def framerate(self, framerate: int) -> None:
        """Set the framerate of the application. Default is 60 FPS."""
        self.m_framerate = min(max(0, framerate), 360)

    @property
    def surface(self) -> pygame.Surface:
        """Get the MainWindow Surface."""
        return self.m_surface

    @property
    def showFPS(self) -> bool:
        """True if FPS are displayed; False otherwise."""
        return self.m_showFPS

    @showFPS.setter
    def showFPS(self, show: bool) -> None:
        """True if FPS are displayed; False otherwise."""
        self.m_showFPS = show

    def resize(self, width: int, height: int) -> None:
        """Resize the MainWindow."""
        pygame.display.set_mode((width, height), pygame.RESIZABLE)

    def update(self) -> None:
        """Update the content of the MainWindow and wait for the next frame."""
        self.m_clock.tick(self.m_framerate)

        if self.m_showFPS:
            self.m_surface.blit(self.updateFPS(), (10,0))

        pygame.display.flip()

    def updateFPS(self) -> None:
        """Update the FPS to be drawn on screen."""
        fpsString: str = str(int(self.m_clock.get_fps()))
        fpsText = self.m_fpsFont.render(fpsString, 1, pygame.Color(255, 255, 255))
        return fpsText
