#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read()

x = 0
y = 0
houses = {'0,0': 1}
for move in input:
  if move == '^':
    y += 1
  elif move == 'v':
    y -= 1
  elif move == '>':
    x += 1
  elif move == '<':
    x -= 1

  if f'{x},{y}' in houses:
    houses[f'{x},{y}'] += 1
  else:
    houses[f'{x},{y}'] = 1

print(len([1 for h in houses if houses[h] >= 1]))
