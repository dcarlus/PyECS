from enum import Enum


class Direction(Enum):
    """Available directions for a 2D game."""
    UP = 1 << 0
    DOWN = 1 << 1
    LEFT = 1 << 2
    RIGHT = 1 << 3
    UP_LEFT = UP | LEFT
    UP_RIGHT = UP | RIGHT
    DOWN_LEFT = DOWN | LEFT
    DOWN_RIGHT = DOWN | RIGHT

    @classmethod
    def contains(cls, value):
        return value in cls._value2member_map_