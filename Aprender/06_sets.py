### Sets ###
### Un set no es una estrucutra ordenada, por tanto no podemos acceder por índice
### Un set no admite valores repetidos

my_set_a = set() # Declaramos un set
my_set_b = {} # Declaramos un set. Inicialmente lo declara como diccionario, hasta que añadamos algún elemento

my_set_b = {'Raúl', 'García', 50}

print('my_set_a = ', my_set_a)
print('my_set_b = ', my_set_b)

print('my_set_a len = ', len(my_set_a))
print('my_set_b len = ', len(my_set_b))

# Añadimos un elemento, pero se inserta en una posición aleatoria, sin orden
my_set_b.add('Madrid')
print('my_set_b = ', my_set_b)

# Un set no admite repetidos. Por tanto un segundo valor igual no lo inserta
my_set_b.add("Madrid")
print('my_set_b = ', my_set_b)

# Así preguntamos si un elemento está en el set
print('Raúl' in my_set_a)
print('Raúl' in my_set_b)

# Añade el valor de un set a otro set
my_set_a.update(my_set_b)
print('my_set_a = ', my_set_a)

# Pasamos el set a una lista
my_list_a =list(my_set_a)
print('my_lis_a = ', my_set_a)

my_set_c = {'Python', 'Java', 'Pascal', 'Cobol'}

# Creamos un nuevo set de la unión de dos. Si unimos mas veces lo mismo, recordemos que no se repiten
my_set_d = my_set_a.union(my_set_c)
print('my_set_d = ', my_set_d)
my_set_d = my_set_a.union(my_set_c).union(my_set_c).union("Cobol")
print('my_set_d = ', my_set_d)

# Así podemos ver las diferencias de dos set
print(my_set_d.difference(my_set_c))
