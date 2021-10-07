import pygame
from engine.direction import Direction
from engine.geometry import Point


class Animation:
    """Animation of a Sprite."""

    def __init__(
            self,
            yPositions: {Direction, int},
            width: int,
            amountSprites: int
    ):
        """Create a new Animation instance."""
        realYPositions: {Direction, int} = {}

        for dir, y in yPositions.items():
            if Direction.contains(dir) and y >= 0:
                realYPositions[dir] = y

        self.m_yPositions: {Direction, int} = realYPositions
        self.m_amountSprites: int = max(1, amountSprites)
        self.m_width = max(0, width)
        self.m_currentDirection: Direction = Direction.UP
        self.m_currentIndex: int = 0

    def activate(self) -> None:
        """Activate the current Animation."""
        self.m_currentIndex = 0

    def nextSprite(self) -> None:
        """Prepare for the next frame drawing of the Sprite (do not draw!)."""
        self.m_currentIndex = (self.m_currentIndex + 1) % self.m_amountSprites

    @property
    def direction(self) -> Direction:
        """Get the current direction of the Animation."""
        return self.m_currentDirection

    @direction.setter
    def direction(self, direction: Direction) -> None:
        """Set the current direction of the Animation."""
        if Direction.contains(direction) and self.m_yPositions.__contains__(direction):
            self.m_currentDirection = direction

    def yPosition(self, height: int) -> int:
        """Get the Y position of the Animation in the sprite sheet for a given Direction."""
        if self.m_yPositions.__contains__(self.m_currentDirection):
            return self.m_yPositions[self.m_currentDirection] * height
        return 0

    @property
    def xPosition(self) -> int:
        return self.m_width * self.m_currentIndex


class Sprite(pygame.sprite.Sprite):
    """Convenient way to use PyGame sprites."""

    SpriteSheets: {str, pygame.image} = {}

    def __init__(
            self,
            spriteSheet: str = '',
            width: int = 0,
            height: int = 0,
            colorKey: [] = [0, 0, 0],
            framerate: int = 20
    ) -> None:
        """Create a new Sprite instance."""
        super().__init__()

        if len(spriteSheet):
            if spriteSheet not in Sprite.SpriteSheets:
                Sprite.SpriteSheets[spriteSheet] = pygame.image.load(spriteSheet)

            self.m_sheet: pygame.image = Sprite.SpriteSheets[spriteSheet]
            self.m_spriteWidth: int = max(0, width)
            self.m_spriteHeight: int = max(0, height)
            self.m_colorKey: [] = colorKey
            self.m_framerate: int = max(0, framerate) + 1
            self.m_frameCounter: int = 0

            self.m_animations: {str, Animation} = {}
            self.m_currentAnimation: Animation = None
            self.m_needUpdate: bool = False

            self.image: pygame.Surface = pygame.Surface([self.m_spriteWidth, self.m_spriteHeight])
            self.rect: pygame.Rect = self.image.get_rect()
            self.update()

    def addAnimation(
            self,
            name: str,
            yPositions: {Direction, int},
            amountSprites: int
    ) -> None:
        """Add a new animation extracted from the sprite sheet. The animation is read on a row containing the specified
        amount of sprites. A name is given to the animation to have an easier referencing.
        Notice that all the directions must have the same amount of sprites in the sprite sheet."""
        self.m_animations[name] = Animation(yPositions, self.m_spriteWidth, amountSprites)

    def changeAnimation(self, animName: str) -> None:
        """Change the current Animation."""
        if self.m_animations.__contains__(animName):
            if self.m_currentAnimation is self.m_animations[animName]:
                return

            if self.m_currentAnimation is not None:
                previousDirection: Direction = self.m_currentAnimation.direction
                self.m_animations[animName].direction = previousDirection
            self.m_currentAnimation = self.m_animations[animName]
            self.m_currentAnimation.activate()
            self.m_needUpdate = True
        else:
            self.m_currentAnimation = None

    def changeDirection(self, direction: Direction) -> None:
        """Change the direction of the current Animation."""
        if self.m_currentAnimation.direction == direction:
            return

        self.m_currentAnimation.direction = direction
        self.m_needUpdate = True

    def update(self) -> None:
        """Get the sprite to be rendered in the current Animation."""
        if self.m_currentAnimation is None:
            return

        self.m_frameCounter = (self.m_frameCounter + 1) % self.m_framerate

        if not self.m_needUpdate or self.m_frameCounter != 0:
            return

        if self.m_frameCounter == 0:
            self.m_currentAnimation.nextSprite()

        xSheet = self.m_currentAnimation.xPosition
        ySheet = self.m_currentAnimation.yPosition(self.m_spriteHeight)
        Destination: (int, int) = (0, 0)

        self.image.fill(self.m_colorKey)
        self.image.blit(
            self.m_sheet,
            Destination,
            [xSheet, ySheet, self.m_spriteWidth, self.m_spriteHeight]
        )

        self.image.set_colorkey(self.m_colorKey)
        self.m_needUpdate = False

    def isAlreadyInDirection(self, direction: Direction) -> bool:
        """Check if the Sprite is already set on the animation for the given Direction."""
        return self.m_currentAnimation.direction == direction

    def collides(self, other: 'Sprite') -> bool:
        """Test if the current Sprite collides another one."""
        return self.rect.colliderect(other.rect)

    @property
    def position(self) -> Point:
        """Get the current position of the Sprite (in the 2D game world)."""
        return Point(self.rect.x, self.rect.y)

    @position.setter
    def position(self, position: Point) -> None:
        """Set the position of the Sprite (in the 2D game world)."""
        self.rect.topleft = position.asTuple()
        self.m_needUpdate = True

    @property
    def ready(self) -> bool:
        return self.image is not None
