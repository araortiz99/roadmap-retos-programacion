"""
    EJERCICIO:
    1) Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
        Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
        (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
    2) Utilizando las operaciones con operadores que tú quieras, crea ejemplos
        que representen todos los tipos de estructuras de control que existan
        en tu lenguaje:
        Condicionales, iterativas, excepciones...
    *Debes hacer print por consola del resultado de todos los ejemplos.

    DIFICULTAD EXTRA (opcional):
    3)  Crea un programa que imprima por consola todos los números comprendidos
        entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""


var1 = 8
var2 = 5

#1 Operadores aritméticos
print(f"Operadores aritméticos")
print(f"Suma: {var1} + {var2} = {var1 + var2}")
print(f"Resta: {var1} - {var2} = {var1 - var2}")
print(f"Multiplicación: {var1} * {var2} = {var1 * var2}")
print(f"División: {var1} / {var2} = {var1 / var2}")
print(f"Módulo: {var1} % {var2} = {var1 % var2}")
print(f"Potencia: {var1} ** {var2} = {var1 ** var2}")
print(f"División entera: {var1} // {var2} = {var1 // var2}")

#2 Operadores de comparación
print(f"Operadores de Comparación")
print(f"Igualdad: {var1} == {var2} es {var1 == var2}")
print(f"Diferencia: {var1} != {var2} es {var1 != var2}")
print(f"Mayor que: {var1} > {var2} es {var1 > var2}")
print(f"Menor que: {var1} < {var2} es {var1 < var2}")
print(f"Mayor o igual que: {var1} >= {var2} es {var1 >= var2}")
print(f"Menor o igual que: {var1} <= {var2} es {var1 <= var2}")

#3 Operadores lógicos
print(f"Operadores lógicos")
print (f"{var1} > 13 AND && {var2} < 10 : {var1 > 3 and var2 < 10}")
print (f"{var1} > 13 OR {var2} < 10 : {var1 > 3 or var2 < 10}")
print (f"NOT ! {var2} < 10 : {not var2 < 10}")

#4 Operadores de asignación
print(f"Operadores de asignación")
var1 =8      # Asignación
var1 += var2 # Suma en asignación
var1 -= var2 # Resta en asignación
var1 *= var2 # Multiplicación en asignación
var1 /= var2 # División en asignación
var1 %= var2 # Módulo en asignación
var1 //= var2 # División entera en asignación
var1 **= var2 # Exponente en asignación

#5 Operadores de identidad
print(f"Operadores de identidad")
var3 = 8.0
new_var3 = 9.0
print(f"mi número era {float(var3) } pero mi nro actual es {new_var3} : {var3 is new_var3}")

#6 Operadores de pertenencia
print(f"Operadores de pertenencia")
print(f" 'u' in 'moure' = {'u' in 'moure'}") #IN
print(f" 'u' not in 'moure' = {'u' in 'moure'}") #NOT IN

#7 Operadores de bits
print(f"Operadores de bits")
a = 60          
b = 13            
print(f"AND & : {a & b}")