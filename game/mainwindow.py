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

        if icon is not None:
            pygame.display.set_icon(icon)

    @staticmethod
    def end() -> None:
        """End the game application."""
        print('Quit {}'.format(pygame.display.get_caption()[0]))
        pygame.quit()

    def resize(self, width: int, height: int):
        """Resize the MainWindow."""
        pygame.display.set_mode((width, height), pygame.RESIZABLE)

    def draw(self):
        """Update the content of the MainWindow."""
        pygame.display.flip()
