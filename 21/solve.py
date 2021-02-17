#!/bin/python3

from collections import defaultdict, deque
from sys import stdin

data = [line.strip() for line in stdin.readlines()]


foods = []
for line in data:
    ingredients, allergens = line.split('(')
    ingredients = ingredients.split(' ')[:-1]
    allergens = allergens.replace(')', '').replace(',', '').split(' ')[1:]
    foods.append((ingredients, allergens))


sets = dict()
total = set()
counts = defaultdict(int)

for ingredients, allergens in foods:
    total = total.union(set(ingredients))
    for ingredient in ingredients:
        counts[ingredient] += 1
    for allergen in allergens:
        if allergen not in sets:
            sets[allergen] = set(ingredients)
        else:
            current = sets[allergen]
            other = set(ingredients)
            sets[allergen] = current.intersection(other)


# part 1
inert = total.copy()
for ingredients in sets.values():
    inert -= ingredients

amount = sum(counts[item] for item in inert)

print(amount)


# part 2
ones = deque()
more = dict()

for allergen, ingredients in sets.items():
    if len(ingredients) == 1:
        ones.append((allergen, ingredients))
    else:
        more[allergen] = ingredients

result = []
while ones:
    current = ones.popleft()
    for allergen, ingredients in list(more.items()):
        ingredients.difference_update(current[1])
        if len(ingredients) == 1:
            ones.append((allergen, ingredients))
            del more[allergen]
    result.append(current)

ingredients = []
for _, ingredient_set in sorted(result, key=lambda o: o[0]):
    ingredients.append(ingredient_set.pop())

print(','.join(ingredients))

































