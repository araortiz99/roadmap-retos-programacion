#  EJERCICIO:
#  * - Crea ejemplos de funciones básicas que representen las diferentes
#  *   posibilidades del lenguaje:
#  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
#  * - Comprueba si puedes crear funciones dentro de funciones.
#  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
#  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#  *
#  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
#  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.


#Funciones definidas por el usuario

#Funciones Simples
nombre = "Yerilim"
def saludar(nombre):
    print(f"¡Hola, bienvenido {nombre}!")   

saludar(nombre)

#Funciones con retorno
def return_saludo(nombre):
    return "Hola, bienvenido " + nombre 

vr_saludo = return_saludo(nombre)
print(vr_saludo)

#Funciones con parámetros
def arg_saludo(nombre, saludo):
    return saludo + nombre

#Con argumentos y retornos
def return_arg_saludo(saludo, nombre):
    return f"{saludo}, {nombre}!"

print(return_arg_saludo("Hi", "Yerilin"))

#Con retorno de varios valores

def multiple_return_greet(nombre):
    return "Hola", nombre

saludo, nombre = multiple_return_greet("Yerilin")
print(saludo)
print(nombre)

#Con un nro variable de argumentos
def variable_arg_saludo(*nombres): # *nombres es un argumento de longitud variable
    for nombre in nombres:  # nombres es una tupla
        print(f"Hola, {nombre}!")   

variable_arg_saludo("Yerilin", "Ruth", "Andrea")    

#Con un nro variable de argumentos con palabras clave
def many_variables_key(**pokemons): # **nombres es un argumento de longitud variable
    for key, value in pokemons.items():  
        print(f" {value} es el ({key})")

many_variables_key(
    nombre = "Pikachu",
    tipo = "Electrico",
    entrenador = "Ash",
    nivel = 100
)


#Funciones dentro de funciones
def outside_func():
    def inside_func():
        print("Soy una función dentro de otra función")
    inside_func()

outside_func()

#Funciones del lenguaje
#Existen muchas funciones por defecto de Python, aca se mostraran algunas no mas. 
#Para mas informacion: https://docs.python.org/es/3.9/library/functions.html#len
    
print(len("Hola")) #4
print(abs(-1)) #1
print(round(3.1416)) #3
print(type(3)) #<class 'int'>
print(isinstance(3, int)) #True
print(max(1,2,3,4)) #4
print(min(1,2,3,4)) #1
print(sum([1,2,3,4])) #10
print(pow(2,3)) #8
print(chr(65)) #A
print(ord("A")) #65
print(bin(10)) #0b1010
print(hex(10)) #0xa
print(oct(10)) #0o12
print(str(10)) #10
print(float(10)) #10.0
print(bool(1)) #True
print(bool(0)) #False
print(list((1,2,3))) #[1, 2, 3]
print(tuple([1,2,3])) #(1, 2, 3)
print(set([1,2,3])) #{1, 2, 3}
print(dict(a=1, b=2, c=3)) #{'a': 1, 'b': 2, 'c': 3}

 # Variables globales y locales. / Local and global variables.
""" 
    Las variables globales son las que se crean simplemente al crear una fuera de cualquier tipo de 
    estructura de control o similar del lenguage, y se pueden acceder desde cualquier parte del codigo. 
    Mientras que las locales son las que se crean cuando usas variables dentro de funcion, o similar, 
    pero que no se pueden "ver" desde otra parte del codigo que no sea dentro de donde fue declara.
"""

#Variable global
global_variable = "Yerilin"
print(global_variable)

def func():
    local_var = "Hola"
    print(f" {local_var}, {global_variable}")

func()

#Dificultad Extra

#print numbers fizz buzz

def print_numbers (string1, string2) -> int:
    count = 0   
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(string1 + string2)
        elif number % 3 == 0:
            print(string1)
        elif number % 5 == 0:
            print(string2)
        else:  
            print(number)
            count += 1
    print (f"Total de números: {count}")

print(print_numbers("Fizz", "Buzz"))



