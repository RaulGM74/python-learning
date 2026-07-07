### Diccionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Raúl", "Apellido":"García", "Edad":50, 1:"Python"}
my_dict = {
    "Nombre":"Raúl",
    "Apellido":"García",
    "Edad":50,
    "Lenguajes": {"Python", "C++", "lisp"},
    1:1.90
    }

print(my_dict)

print(len(my_other_dict))

print(my_dict["Nombre"])
my_dict["Nombre"] = "David"
my_dict["Calle"] = "Calle Raúl"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

### Comprobar si una etqiueta está en el diccionario
print("Nombre" in my_dict) # True
print("David" in my_dict) # False

print(my_dict.items()) # Listado de todos los items
print(my_dict.keys()) # Listado de las claves
print(my_dict.values()) # Listdo de los valores

# Crear un diccionario sin valores
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

# Ejemplo de crear un diccionario desde una lista
my_list = ["Nombre", 1, "Piso"]
my_new_dict2 = dict
my_new_dict2 = dict.fromkeys(my_list)
print(my_new_dict2)

# Crear un diccionario copiado de otro
my_new_dict3 = dict.fromkeys(my_dict)
print(my_new_dict3)

# Crear un diccionario copiado de otro. A todas las claves les mete el mismo valor
my_new_dict3 = dict.fromkeys(my_dict, "Dato Ejemplo")
print(my_new_dict3)

# Crear un diccionario copiado de otro.
my_new_dict3 = dict.fromkeys(my_dict)
print(my_new_dict3)





                 