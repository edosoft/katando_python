#!/usr/bin/env python3
# -*- coding utf-8 -*-

def roman_to_arabic(number_r):
  
  r_a = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
  roman_total = 0
  
  for i in range(len(number_r)-1):
    #roman_total += r_a[number_r[i]]
    if r_a[number_r[i]] < r_a[number_r[i+1]]:
      roman_total -= r_a[number_r[i]]
    else:
      roman_total += r_a[number_r[i]]
  
  roman_total += r_a[number_r[-1]]
  
  return roman_total