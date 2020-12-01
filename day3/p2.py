#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read()

sx = 0
rx = 0
sy = 0
ry = 0
turn = True
houses = {'0,0': 2}
for move in input:
  if turn == True:
    if move == '^':
      sy += 1
    elif move == 'v':
      sy -= 1
    elif move == '>':
      sx += 1
    elif move == '<':
      sx -= 1
    x = sx
    y = sy
  else:
    if move == '^':
      ry += 1
    elif move == 'v':
      ry -= 1
    elif move == '>':
      rx += 1
    elif move == '<':
      rx -= 1
    x = rx
    y = ry
  turn = not turn
  if f'{x},{y}' in houses:
    houses[f'{x},{y}'] += 1
  else:
    houses[f'{x},{y}'] = 1

print(len([1 for h in houses if houses[h] >= 1]))
