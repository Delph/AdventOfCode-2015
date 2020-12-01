#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read()

floor = 0
for c, i in enumerate(input):
  if i == '(':
    floor += 1
  elif i == ')':
    floor -= 1
  if floor == -1:
    print(c+1)
    break

