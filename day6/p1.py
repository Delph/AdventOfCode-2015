#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()


lights = []
for i in range(1000):
  lights.append([])
  for j in range(1000):
    lights[i].append(False)

for command in input:
  offset = 0
  if command.startswith('turn on'):
    offset = 8
  elif command.startswith('turn off'):
    offset = 9
  elif command.startswith('toggle'):
    offset = 7

  sep = command.index(',')
  startx = int(command[offset:sep])
  starty = int(command[sep+1:command.index(' ', sep)])
  endx = int(command[command.index('through')+8:command.index(',', sep+1)])
  endy = int(command[command.index(',', sep+1)+1:])

  for i in range(startx, endx+1):
    for j in range(starty, endy+1):
      if offset == 8:
        lights[j][i] = True
      elif offset == 9:
        lights[j][i] = False
      else:
        lights[j][i] = not lights[j][i]

on = 0
for row in lights:
  for l in row:
    if l:
      on += 1
print(on)
