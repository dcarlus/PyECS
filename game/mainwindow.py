import pygame

class MainWindow:
    """Main window of the game."""

    def __init__(
        self,
        width: int = 800,
        height: int = 600,
        caption: str = "New window",
        icon: pygame.Surface = None
    ):
        """Create a new MainWindow instance."""
        pygame.init()
        pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.set_caption(caption)
        self.m_framerate: int = 60
        self.m_clock: pygame.time = pygame.time.Clock()

        if icon is not None:
            pygame.display.set_icon(icon)

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

    def resize(self, width: int, height: int) -> None:
        """Resize the MainWindow."""
        pygame.display.set_mode((width, height), pygame.RESIZABLE)

    def update(self) -> None:
        """Update the content of the MainWindow and wait for the next frame."""
        pygame.display.flip()
        self.m_clock.tick(self.m_framerate)
