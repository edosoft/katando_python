#!/usr/bin/env python
# -*- coding: utf-8 -*-

# roman_validator() v1.1
# by Frank Sosa

def roman_validator(number_r):
  import re

  # Expresión regular de un número romano (v5.1)
  # M{0,3}(C(M|D)|D{0,1}C{0,3})(X(C|L)|L{0,1}X{0,3})(I(X|V)|V{0,1}I{0,3})

  roman_pattern = re.compile(r'\bM{0,3}(C(M|D)|D?C{0,3})(X(C|L)|L?X{0,3})(I(X|V)|V?I{0,3})\b',re.I)
  searching = roman_pattern.search(number_r)

  return True if searching.group() != '' else False 