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


def render(state: list[list[int]]):
    render_map = {
        DEAD: ' ',
        ALIVE: u"\u2588"
    }

    for row in state:
        if state.index(row) > 0:
            print('\n')
        for cell in row:
            print(render_map[cell], sep=None, end='')
