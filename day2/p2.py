#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()


total = 0
for present in input:
  [l, w, h] = list(sorted(map(int, present.split('x'))))
  total += 2 * l + 2 * w
  total += l*w*h

print(total)
