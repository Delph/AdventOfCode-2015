#!/usr/bin/python3

import hashlib

#input = 'abcdef'
input = 'iwrupvqb'


n = 1
while True:
  hash = hashlib.md5((input+str(n)).encode('utf-8')).hexdigest()

  if str(hash).startswith('000000'):
    break;
  n += 1
print(n)
