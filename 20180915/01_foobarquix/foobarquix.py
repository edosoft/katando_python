#!/usr/bin/env python3
# -*- coding utf-8 -*-
def foobarquix(num):
  fbq = {3:'Foo',5:'Bar',7:'Quix'}
  result = ''
  if (num % 3) == 0:
    result += 'Foo'
  if (num % 5) == 0:
    result += 'Bar'
  if (num % 7) == 0:
    result += 'Quix'
  for caracter in str(num):
    if int(caracter) in list(fbq.keys()):
      result += fbq[int(caracter)]

  return result if result else str(num)
