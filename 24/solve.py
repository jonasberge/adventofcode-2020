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
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def neighbour(self, where):
        x, y = self.x, self.y
        # use integers instead of floats
        if where == 'e':
            x -= 4 # 2c
        elif where == 'w':
            x += 4 # 2c
        else:
            if 'e' in where: x -= 2 # 1c
            if 'w' in where: x += 2 # 1c
            if 'n' in where: y += 3 # 3c/2
            if 's' in where: y -= 3 # 3c/2
        return Tile(x, y)

    def neighbours(self):
        return set([
            self.neighbour('e'), self.neighbour('w'),
            self.neighbour('ne'), self.neighbour('nw'),
            self.neighbour('se'), self.neighbour('sw')
        ])

    def __eq__(self, other): return self.x == other.x and self.y == other.y
    def __hash__(self): return hash((self.x, self.y))

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
        tile = tile.neighbour(direction)
    if tile in blacks:
        blacks.remove(tile)
    else:
        blacks.add(tile)


print('1:', len(blacks))


for _ in range(100):
    new_blacks = set()
    for tile in blacks:
        neighbours = tile.neighbours()
        if len(neighbours & blacks) == 1:
            new_blacks.add(tile)
        for neighbour in neighbours:
            if len(neighbour.neighbours() & blacks) == 2:
                new_blacks.add(neighbour)
    blacks = new_blacks

print('2:', len(blacks))

