#!/usr/bin/python3

import string

with open('input.txt') as f:
  input = f.read().splitlines()


def is_nice(str):
  # at least two, non-overlapping groups of two letters
  repeat_double = False
  for i in range(len(str)-1):
    s = str[i:i+2]
    if str.count(s) >= 2:
      repeat_double = True
  if not repeat_double:
    return False

  # three letters of two and one, e.g., xyx
  for i in range(len(str)-2):
    s = str[i:i+3]
    if s[0] == s[2]:
      return True
  return False

#print(f'bkkkkcwegvypbrio is {"nice" if is_nice("bkkkkcwegvypbrio") else "naughty"}')
#print(f'aabcdefgaa is {"nice" if is_nice("aabcdefgaa") else "naughty"}')
#print(f'qjhvhtzxzqqjkmpb is {"nice" if is_nice("qjhvhtzxzqqjkmpb") else "naughty"}')
#print(f'xyxxxx is {"nice" if is_nice("xyxxxx") else "false"}')
#print(f'uurcxstgmygtbstg is {"nice" if is_nice("uurcxstgmygtbstg") else "naughty"}')
#print(f'ieodomkazucvgmuy is {"nice" if is_nice("ieodomkazucvgmuy") else "naughty"}')

nice = 0
for name in input:
  if is_nice(name):
    nice += 1
print(nice)
