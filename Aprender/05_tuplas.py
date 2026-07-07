### Tuplas ###
# Una tupla es un conjunto de valores que NO se pueden modificar

my_tuple_1 = tuple()
my_tuple_2 = ()

my_tuple_1 = (50, 1.90, "Raúl", "García")
my_tuple_2 = (51, 1.60, "MJose", "Aguado")
print(my_tuple_1)
print(type(my_tuple_1))

print(my_tuple_1[0]) # primer elemento
print(my_tuple_1[-1]) # ultimo elemento

print(my_tuple_1.count(1.90)) # mos dice el nº de elemento encontrados
print(my_tuple_1.index('Raúl')) # nos dice el nº de indice de 'Raúl'

#my_tuple_1[1] = 1.88  # no se pueden añadir, eliminar o modificar valores

my_tuple_3 = my_tuple_1 + my_tuple_2
print(my_tuple_3)
print(my_tuple_3[2:4]) # coge elementos 2 a 4 (sin tener en cuenta el 4)

# de esta forma podemos modificar una tupla.
# la cambiamos a lista, la modificamos, y de nueva la hacemos tupla
my_tuple_3 = list(my_tuple_3) # cambia el tipo de tupla a lista
my_tuple_3[4] = 'Hola' # ya podemos operar como lista
my_tuple_3=tuple(my_tuple_3) # ahora lo volvemos a hacer tupla

del my_tuple_3 # Elimina la variable
# print(my_tuple_3) # no podemos hacer esto porque my_tuple_3 ya no existe
