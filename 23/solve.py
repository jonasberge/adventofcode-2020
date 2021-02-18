#!/usr/bin/env python3

from collections import deque
from sys import stdin


data = stdin.read().strip()
cups = [int(c) for c in data]

class Cup:
    def __init__(self, label):
        self.label = label
        self.next = None

    def slice(self, n):
        assert n > 0
        first = self.next
        self.next = None
        current = first
        for _ in range(n - 1):
            current = current.next
            if not current.next:
                # removing all items
                raise Exception
        after = current.next
        current.next = None
        self.next = after
        return first

    def insert(self, head):
        assert head != None
        after = self.next
        self.next = head
        for last in head:
            pass
        last.next = after

    def __iter__(self):
        curr = self
        while True:
            yield curr
            curr = curr.next
            if curr in (self, None):
                break

    def __repr__(self):
        next_value = self.next.label if self.next else None
        return 'Cup({}->{})'.format(self.label, next_value)

class Circle:
    def __init__(self, head):
        self.head = head
        self.current = head
        self.index = dict()
        self._create_index()

    def _create_index(self):
        for cup in self.head:
            self.index[cup.label] = cup

    def slice(self, n):
        sliced = self.current.slice(n)
        for cup in sliced:
            del self.index[cup.label]
        return sliced

    def insert(self, head):
        self.current.insert(head)
        for cup in head:
            self.index[cup.label] = cup

def next_label(label):
    if label == 1:
        return len(cups)
    return label - 1

def print_list(head):
    for cup in head:
        print(cup.label, end=' ')
    print()

# create circle
head = Cup(cups[0])
curr = head
for cup in cups[1:]:
    temp = Cup(cup)
    curr.next = temp
    curr = temp
curr.next = head
circle = Circle(head)

for _ in range(100):
    # pick three cups
    sliced = Circle(circle.slice(3))

    # select next label that is not sliced
    destination = next_label(circle.current.label)
    while destination in sliced.index:
        destination = next_label(destination)

    # insert picked and increment current
    current = circle.current
    circle.current = circle.index[destination]
    circle.insert(sliced.head)
    circle.current = current.next

labels = [cup.label for cup in circle.index[1]]
result = ''.join([str(l) for l in labels])[1:]

print(result)

