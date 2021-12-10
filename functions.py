from random import random, choice

DEAD: int = 0
ALIVE: int = 1


def dead_state(height: int, width: int) -> list[list[int]]:
    return [[DEAD for _ in range(width)] for _ in range(height)]


def random_state(height: int, width: int) -> list[list[int]]:
    return [
        [DEAD if random() >= 0.5 else ALIVE for _ in range(width)]
        for _ in range(height)
    ]


def render(state: list[list[int]]) -> None:
    render_map = {
        DEAD: ' ',
        ALIVE: choice((u'\u259A', u'\u259E'))
    }

    for row in state:
        for cell in row:
            print(render_map[cell], sep=None, end='')
        print('\n')


def next_state(state: list[list[int]]) -> list[list[int]]:
    for x in range(len(state)):
        for y in range(len(state[0])):
            # TODO: calculate live neighbours
            ...
