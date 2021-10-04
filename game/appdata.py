import threading
from engine.mainwindow import MainWindow

class AppData:
    """Aggregation of application data."""
    __Mutex: threading.Lock = threading.Lock()
    __Window: MainWindow = MainWindow(800, 600, 'Crystal Shot', 'resources/ui/cshot_icon.png')

    @staticmethod
    def window() -> MainWindow:
        """Get the main window of the application."""
        return AppData.__Window

    @staticmethod
    def wantAccess() -> None:
        """Lock the access to the data in a multithreading context. Should be always done before accessing data!"""
        AppData.__Mutex.acquire()

    @staticmethod
    def releaseAccess() -> None:
        """Unlock the access to the data in a multithreading context. Should be done just after accessing/modifying
        data!"""
        AppData.__Mutex.release()


class SystemName:
    """For naming Systems."""

    @staticmethod
    def position() -> str:
        return 'Position'

    @staticmethod
    def input() -> str:
        return 'Input'

    @staticmethod
    def sprite() -> str:
        return 'Sprite'

    @staticmethod
    def characterProperties() -> str:
        return 'CharacterProperties'

    @staticmethod
    def ai() -> str:
        return 'AI'


class AnimationName:
    """For naming Animations of Sprites."""

    @staticmethod
    def walk() -> str:
        return 'Walk'

    @staticmethod
    def die() -> str:
        return 'Death'
