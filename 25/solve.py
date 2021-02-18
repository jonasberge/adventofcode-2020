#!/usr/bin/env python3

from collections import deque
from sys import stdin


data = [line.strip() for line in stdin.readlines()]
pk_card = int(data[0])
pk_door = int(data[1])

SUBJECT = 7
MAGIC = 20201227

def generate(subject_number):
    value = 1
    loop_size = 0
    while True:
        loop_size += 1
        value *= subject_number
        value = value % MAGIC
        yield value, loop_size

def loop(subject_number, n):
    gen = generate(subject_number)
    value = subject_number
    for _ in range(n):
        value, _ = next(gen)
    return value

def determine_loop_size(public_key):
    loop = generate(SUBJECT)
    loop_size = 0
    value = -1
    while value != public_key:
        value, loop_size = next(loop)
    return loop_size

ls_card = determine_loop_size(pk_card)
print('ls_card', ls_card)
ls_door = determine_loop_size(pk_door)
print('ls_door', ls_door)

ek_card = loop(pk_door, ls_card)
print('ek_card', ek_card)
ek_door = loop(pk_card, ls_door)
print('ek_door', ek_door)

assert ek_card == ek_door
print('1:', ek_card)

