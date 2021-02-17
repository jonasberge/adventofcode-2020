#!/usr/bin/env python3

from collections import deque
from sys import stdin


data = [line.strip() for line in stdin.readlines()]

one = deque()
two = deque()

for line in data:
    if '1:' in line: current = one
    if '2:' in line: current = two
    if line.isdigit():
        current.append(int(line))

def score(deck):
    acc = 0
    for index, value in enumerate(reversed(deck)):
        acc += (index + 1) * value
    return acc

def combat(one, two):
    while one and two:
        a, b = one.popleft(), two.popleft()
        deck = one if a > b else two
        deck.extend(sorted([a, b], reverse=True))
    return deck

def recursive_combat(one, two):
    history = set()
    while one and two:
        identity = (score(one), score(two))
        if identity in history:
            return 1, one
        history.add(identity)
        a, b = one.popleft(), two.popleft()
        if len(one) >= a and len(two) >= b:
            x = deque(list(one)[:a])
            y = deque(list(two)[:b])
            winner, _ = recursive_combat(x, y)
            top = a if winner == 1 else b
            bot = b if winner == 1 else a
            deck = one if winner == 1 else two
            deck.extend([top, bot])
            continue
        deck = one if a > b else two
        deck.extend(sorted([a, b], reverse=True))
    winner = 1 if one else 2
    return winner, deck


# part 1, commented out because of endless games in part 2
# print(score(combat(one.copy(), two.copy())))

_, deck = recursive_combat(one, two)
print(score(deck))

