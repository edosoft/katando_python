#!/usr/bin/env python3
# -*- coding utf-8 -*-

# arabic_to_roman v1.1
# by Frank Sosa

def arabic_to_roman(number_a):
  a_r = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
  ar_k = list(a_r.keys())

  number_r = ''
  
  miles = int(number_a/1000)
  centenas = int((number_a%1000)/100)
  decenas = int(((number_a%1000)%100)/10)
  unidades = int((((number_a%1000)%100)%10))
  number = [miles,centenas,decenas,unidades]

  for index in range(len(number)):
    idx = 2 * index
    if number[index] == 4:
      number_r += ar_k[idx] + ar_k[idx-1]
    elif number[index] == 9:
      number_r += ar_k[idx] + ar_k[idx-2]
    elif number[index] >= 5:
      number_r += ar_k[idx-1] + (number[index]-5) * ar_k[idx]
    else:
      number_r += number[index] * ar_k[idx]

  return number_r