#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_price(temporadas):
  precio = 5
  descuento = 1
  cantidad=len(temporadas)
  if (cantidad>4):
    descuento = .8
  elif (cantidad>2):
    descuento = .9
  return cantidad*precio*descuento