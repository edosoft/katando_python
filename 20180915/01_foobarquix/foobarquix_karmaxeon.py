#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def foobarquix(number):
  numbers = {3: 'Foo', 5: 'Bar', 7: 'Quix'}
  result = ''
  result += ''.join(text for value, text in numbers.items() if number % value == 0)
  result += ''.join(text for letter in str(number) for value, text in numbers.items() if int(letter) == value)
  return result if result else str(number)
