#!/usr/bin/env python3
# -*- coding utf-8 -*-

def arabic_to_roman(number_a):
  a_r = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
  ar_k = list(a_r.keys())
  ar_v = list(a_r.values())
  number_r = ''
  
  miles = int(number_a/1000)
  centenas = int((number_a%1000)/100)
  decenas = int(((number_a%1000)%100)/10)
  unidades = int((((number_a%1000)%100)%10))
  
  # MILES
  number_r = 'M'*miles
  
  #  CENTENAS
  if centenas == 4:
    number_r += 'CD'
  elif centenas == 9:
    number_r += 'CM'
  elif centenas >= 5:
    number_r += 'D'+ (centenas-5) * 'C'
  else:
    number_r += centenas * 'C'
  
  # DECENAS
  if decenas == 4:
    number_r = 'XL'
  elif decenas == 9:
    number_r += 'XC'
  elif decenas >= 5:
    number_r += 'L'+ (decenas-5) * 'X'
  else:
    number_r += decenas * 'X'


  # UNIDADES
  if unidades == 4:
    number_r += 'IV'
  elif unidades == 9:
    number_r += 'IX'
  elif unidades >= 5:
    number_r += 'V'+ (unidades-5) * 'I'
  else:
    number_r += unidades * 'I'

  return number_r