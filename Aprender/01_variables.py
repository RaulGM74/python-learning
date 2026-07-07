# Variables

print("********************* Inicio programa")
mi_var_int: int

# Definimos variables
mi_var_string = "Mi variable String"
mi_var_int = 4
mi_var_float = float(mi_var_int)
mi_var_bool = True

# Mostrar por pantalla
print(mi_var_string)
print(mi_var_int)
print(mi_var_float)
print(mi_var_bool)
print(mi_var_string, "/", mi_var_int, "/", mi_var_bool)
print("Longitud de 'mi_var_string':", len(mi_var_string))

# Variables en una sola linea. Cuidado con esto
nombre, apellido, edad = "Raúl", 'García', 35

# Pedir datos y mostrar por pantalla
nombre = input("Nombre?")
edad = input("Edad?")

print("Me llamo ", nombre, "y tengo ", edad, "años")

# Cambiar el tipo de varible. Python no tiene un tipado fuerte
print(type(nombre)) # Tipo 'str'
nombre = 53
print(type(nombre)) # Tipo 'int'

# forzar un tipo de dato. Esto no hace nada, varA será 'int'
varA: str = 35
print(type(varA))

print("********************* Fin programa")