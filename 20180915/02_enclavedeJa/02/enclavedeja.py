#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#temporadas = [4,4,3,4,3,2,4,3,2,1]
def get_price(temporadas):
  # Diccionario de temporadas y sus precios unitarios  
  precios_temporadas = {0:3, 1:3.5, 2:4, 3:4.5, 4:5 }
  descuentos_num_temporadas = {1:0, 2:0, 3:10, 4:20, 5:30}
  # En 'cantidades' guardamos un diccionario con la temporada y el número de veces que sale
  cantidades = {}
  for x in precios_temporadas.keys():
      cantidades[x] = temporadas.count(x)
  """
  'cantidades.keys()' equivale al número de la temporada...
  ... y 'cantidades.values()' a la cantidad de esa temporada que se compra
  """
  
  
  coleccion_precio =
  return total
  """
  temporadas = [1,1,2,1,2,3,1,2,3,4]

# Diccionario de temporadas y sus precios unitarios  
precios_temporadas = {0:3, 1:3.5, 2:4, 3:4.5, 4:5 }
descuentos_num_temporadas = {1:0, 2:0, 3:10, 4:20, 5:30}
# En 'cantidades' guardamos un diccionario con la temporada y el número de veces que sale
cantidades = {}
for x in precios_temporadas.keys():
  cantidades[x] = temporadas.count(x)

cantidades
# temporada que hay en todas las colecciones
cantidades.get(max(cantidades.values()))
# precio de esa temporada
precios_temporadas.get(cantidades.get(max(cantidades.values())))
  """