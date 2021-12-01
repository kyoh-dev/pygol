from random import random

DEAD: int = 0
ALIVE: int = 1


def dead_state(width: int, height: int) -> list[list[int]]:
    return [[DEAD for _ in range(width)] for _ in range(height)]


def random_state(width: int, height: int) -> list[list[int]]:
    return [
        [DEAD if random() >= 0.5 else ALIVE for _ in range(width)]
        for _ in range(height)
    ]
