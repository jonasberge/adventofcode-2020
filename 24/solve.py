#!/usr/bin/env python3

from collections import deque
from sys import stdin


data = [line.strip() for line in stdin.readlines()]


# store integer coordinates of tiles
# https://en.wikipedia.org/wiki/Hexagonal_tiling
# https://socratic.org/questions/what-is-the-area-of-a-hexagon-where-all-sides-are-8-cm
# distance of centers horizontally (e, w): (2c, 0) = (x, y) offsets
# distance of centers diagonally (ne, nw, ...): (1c, 3c/2)
class Tile:
    def __init__(self):
        self.x = 0
        self.y = 0

    @property
    def pos(self):
        return (self.x, self.y)

    def step(self, where):
        # use integers instead of floats
        if where == 'e':
            self.x -= 4 # 2c
            return
        if where == 'w':
            self.x += 4 # 2c
            return
        if 'e' in where: self.x -= 2 # 1c
        if 'w' in where: self.x += 2 # 1c
        if 'n' in where: self.y += 3 # 3c/2
        if 's' in where: self.y -= 3 # 3c/2

    def __repr__(self):
        return 'Tile({}, {})'.format(self.x, self.y)


def iterate_steps(line):
    chars = deque(line)
    while chars:
        current = chars.popleft()
        if current in ('s', 'n'):
            yield current + chars.popleft()
        else:
            yield current

blacks = set()
for line in data:
    tile = Tile()
    for direction in iterate_steps(line):
        tile.step(direction)
    if tile.pos in blacks:
        blacks.remove(tile.pos)
    else:
        blacks.add(tile.pos)


print(len(blacks))
