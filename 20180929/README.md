## Intro

Vamos a hacer un ejercicio clásico y es jugar con los números romanos y árabes.

Como refresco, vamos a ver sus símboles y reglas.

### Sistema Romano
#### Símbolos

 Romano | Árabe 
--------|-------
 I | 1 
 V | 5 
 X | 10 
 L | 50 
 C | 100 
 D | 500 
 M | 1000 

#### Reglas

Sólo se contemplan números entre el 1 y el 3999

* Los símbolos I, X, C y M se pueden repetir hasta tres veces.
* Los símbolos V, L y D no pueden repetirse.
* Los símbolos I, X y C se suman si están a la derecha de otro mayor o igual.
* Los símbolos I, X y C se restan si están a la izquierda de otro mayor y solamente pueden anteponerse a los dos símbolos que le siguen en la sucesión.
* I se resta de V y X
* X se resta de L y C
* C se resta de D y M
* Los símbolos V, L y D no pueden colocarse a la izquierda de otro mayor.

### Iteraciones

#### Primera

* [Pasar de número romanos a árabes](01_roman_to_arabic/test_roman_to_arabic.py)
* [Pasar de árabes a romanos](02_arabic_to_roman/test_arabic_to_roman.py)
* [Hacer un validador de números romanos](03_roman_validator/test_roman_validator.py)
