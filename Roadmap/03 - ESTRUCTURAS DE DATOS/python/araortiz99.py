"""
* EJERCICIO:
- Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
- Utiliza operaciones de inserción, borrado, actualización y ordenación.

* DIFICULTAD EXTRA (opcional):
- Crea una agenda de contactos por terminal.
 - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 - Cada contacto debe tener un nombre y un número de teléfono.
 - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
   los datos necesarios para llevarla a cabo.
 - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
   (o el número de dígitos que quieras)
 - También se debe proponer una operación de finalización del programa.
"""

#Listas []
mi_lista = ["Yerilin", "Ruth", "Andrea", "Ara"]
print(type(mi_lista))
print(mi_lista)
mi_lista.append("Ortiz")  # Append Inserción
print(mi_lista)
mi_lista.remove("Ruth")  # Remove Borrado
print(mi_lista)
mi_lista[3] = "Lady"  # Actualiza el valor en la posición 4
print(mi_lista)
mi_lista.sort()  # Ordena la lista en orden ascendente
print(mi_lista)
mi_lista.sort(reverse=True)  # Ordena la lista en orden descendente
print(mi_lista)


#Tuplas() (solo permite operaciones de acceso)
    #Estructura inmutable
mi_tupla = ("Yerilin", "Ruth", "Andrea", "Ara")
print(type(mi_tupla))
print(mi_tupla[0])
mi_tupla = sorted(mi_tupla)  # Ordena la tupla convirtiéndola a lista
print(type(mi_tupla))
mi_tupla = tuple(sorted(mi_tupla))  # Convierte la lista ordenada en tupla
print(type(mi_tupla))


#Sets {} Son estructuras desordenadas y NO permiten elementos duplicados
mi_set = {"Yerilin", "Ruth", "Andrea", "Ara"}
print(type(mi_set))
print(mi_set)
mi_set.add("Ortiz")  # Inserta un elemento
print(mi_set)
mi_set.remove("Ruth")  # Elimina un elemento
print(mi_set)
mi_set.update(["Lady", "Yerilin"])  # Inserta varios elementos
print(mi_set)
mi_set = set(sorted(mi_set))  #No se puede ordenar un set, pero se puede convertir a lista y ordenarla

print(type(mi_set))


#Diccionarios {} Son estructuras que permiten almacenar pares clave-valor
mi_diccionario: dict = { 
    "nombre": "Yerilin", 
    "apellido": "Baez", 
    "alias": "Lady",
    "edad": 30 
}

print(mi_diccionario["nombre"]) # Acceso a un valor por clave
mi_diccionario["email"] = "yerilinbaez@dev.com" # Inserción
mi_diccionario["edad"] = 31 # Actualización
del mi_diccionario["alias"] # Borrado
mi_diccionario = dict(sorted(mi_diccionario.items())) # Ordenación(se convierte a tuplas ordenadas y luego se vuelve a diccionario)
print(type(mi_diccionario))

#CREA UNA AGENDA DE CONTACTOS

def mi_agenda():

    agenda : dict = {}  
    
    def insertar_contacto():
        telefono = input("Teléfono de contacto: ")
        if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 11:
            agenda[nombre] = telefono
            print("Contacto agregado correctamente")
        else:
            print("Número de teléfono no válido. Debe ser numérico y tener 11 dígitos como máximo.")
          


    while True:

        print("")
        print("Bienvenido a tu agenda de contactos")
        print("Selecciona una opción:")
        print("1. Ver contactos")
        print("2. Agregar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("\nOpción: ")

        match opcion:
            case "1":
                print("Ver contactos")
                if nombre in agenda:
                    print(f"{nombre}: {agenda[nombre]}")
                else:
                    print("No se han encontrado contactos")

            case "2":
                print("Agregar contacto")
                nombre = input("Nombre de contacto: ")
                insertar_contacto()

            case "3":
                print("Actualizar contacto")
                nombre = input("Nombre de contacto a actualizar: ")
                if nombre in agenda:
                    insertar_contacto()
                else:
                    print("No se ha encontrado el contacto")

            case "4":
                print("Eliminar contacto")
                nombre = input("Nombre de contacto a eliminar: ")
                if nombre in agenda:
                    del agenda[nombre]
                    print("Contacto eliminado correctamente")

            case "5":
                print("Saliendo de la agenda...")
                break

            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")

mi_agenda()