#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read().splitlines()


total = 0
for present in input:
  [l, w, h] = list(map(int, present.split('x')))

  total += 2*l*w + 2*w*h + 2*h*l

  lw = l*w
  wh = w*h
  hl = h*l

  total += min([lw, wh, hl])
print(total)
