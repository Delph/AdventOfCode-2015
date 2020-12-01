#!/usr/bin/python3

with open('input.txt') as f:
  input = f.read()

print(input.count('(') - input.count(')'))
