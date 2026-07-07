### Lists ###

# dos formas de definir listas
my_list_1 = list()
my_list_2 = []

print(type(my_list_2)) # las listas son de class 'list'
print("Nº de elementos lista: ", len(my_list_1)) # lista vacia, 0 elementos

my_list_1 = [51, 50, 17, 15, 15]
print("Nº de elementos lista: ", len(my_list_1))

my_list_2 = [50, 1.90 , "Raúl" , "García"]

print(my_list_2[0])     # accedemos a posición 1 de la lista
print(my_list_2[3])     # accedemos a posición 4 de la lista
#print(my_list_2[8])    # accedemos a posición 9 de la lista --> Error
print(my_list_2[-1])    # ultima de la lista (-1, -2, etc.)
print(my_list_2[3])     # penultima de la lista

print(my_list_1.count(15)) # cuenta los valores que encuentra

edad, altura, nombre, apellido = my_list_2 # vuelca valores de la lista en variables
print(edad, altura, nombre, apellido)

print(my_list_1 + my_list_2)    # se pueden concatenar listas

my_list_2.append("PagoNxt")     # añade un elemento al final de la lista
print(my_list_2)

my_list_2.insert(1,"Madrid")    # inserta en la posicion 1 un elemento
print(my_list_2)

my_list_2.remove("Madrid")      # elimina "Madrid" de la lista
print(my_list_2)

del my_list_2[2]                # elimina por indice, en este caso el 2
print(my_list_2)

my_list_2[1] = "Verde"          # cambia el valor del elemento 1
print(my_list_2)

print(my_list_2.pop(2))         # elimina elemento 2
print(my_list_2)

my_list_2_new = my_list_2.copy() # copia una lista en otra

my_list_2_new.reverse()         # invierte la lista
print(my_list_2_new)

my_list_1.sort() # orden una lista de menor a mayor. Se le pueden poner criterios
print(my_list_1)

print(my_list_2.pop()) # elimina el ultimo elemento de la lista
print(my_list_2)

my_list_2.clear() # borra la lista completa
print(my_list_2)

my_list_1 = "Hola Python"
print(my_list_1) # esto cambia el tipo de variabe de list a string






