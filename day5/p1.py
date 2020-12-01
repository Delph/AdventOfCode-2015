#!/usr/bin/python3

import string

with open('input.txt') as f:
  input = f.read().splitlines()


def is_nice(str):
  # bad strings
  bad_str = ['ab', 'cd', 'pq', 'xy']
  for b in bad_str:
    if b in str:
      return False

  # check for double letters, e.g., 'aa'
  double = False
  for c in string.ascii_lowercase:
    if c * 2 in str:
      double = True
  if not double:
    return False

  # check for three vowels
  vowels = 0
  for v in ['a', 'e', 'i', 'o', 'u']:
    vowels += str.count(v)
  return vowels >= 3


#print(f'ugknbfddgicrmopn is {"nice" if is_nice("ugknbfddgicrmopn") else "naughty"}')
#print(f'aaa is {"nice" if is_nice("aaa") else "naughty"}')
#print(f'jchzalrnumimnmhp is {"nice" if is_nice("jchzalrnumimnmhp") else "naughty"}')
#print(f'haegwjzuvuyypxyu is {"nice" if is_nice("haegwjzuvuyypxyu") else "naughty"}')
#print(f'dvszwmarrgswjxmb is {"nice" if is_nice("dvszwmarrgswjxmb") else "naughty"}')

nice = 0
for name in input:
  if is_nice(name):
    nice += 1
print(nice)
