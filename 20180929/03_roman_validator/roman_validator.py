#!/usr/bin/env python
# -*- coding: utf-8 -*-

# roman_validator() v1
# by Frank Sosa

def roman_validator(number_r):
  import re
  validator = False
  # Expresión regular de un número romano (v4.0)
  # M{0,3}(C(M|D)|DC{0,3}){0,1}(X(C|L)|LX{0,3}){0,1}(I(X|V)|VI{0,3}){0,1}

  roman_pattern = re.compile(r'\bM{0,3}(C(M|D)|DC{0,3})?(X(C|L)|LX{0,3})?(I(X|V)|VI{0,3})?\b',re.I)
  searching = roman_pattern.search(number_r)

  if searching.group() != '':
    validator = True
  return validator