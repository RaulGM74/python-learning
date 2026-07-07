# String

string_a = "string A"
string_b = 'string BB'

print(len(string_a))
print(len(string_b))

print(string_a + " " + string_b)

string_c = "String con \n salto de linea"
print(string_c)

string_d = "\t String con tabulación"
print(string_d)

string_e = "\\t String con escapado y \n salto de linea"
print(string_e )

# Formateos de cadenas
nombre = "Raúl"
apellido = "García"
edad = 50
print("Soy %s %s y tengo %d años" %( nombre, apellido, edad))       # Formateo elegante
print("Soy {} {} y tengo {} años".format( nombre, apellido, edad))  # Formateo elegante
print(f"Soy {nombre} {apellido} y tengo {edad} años")               # Formateo elegante. Es la mejor forma

# Desempaquetado de caracteres
lenguaje = 'Python'
a = lenguaje
b = lenguaje
c1, c2, c3, c4, c5, c6 = lenguaje
print(a)
print(b)
print(c1, c2, c3, c4, c5, c6)

# División
print("\n")
lenguage_slice = lenguaje[1:3]  # coge 3 caracteres desde el 1
print(lenguage_slice)
print(lenguaje[1:])             # coge desde el 1 hasta el final
print(lenguaje[-2])             # coge quitando -2 desde el final 
print(lenguaje[::-1])           # cadena en reverse
print(lenguaje[0:6:2])          # coge 5 desde el 0 y ...

# Funciones
print("\n")
print(lenguaje.capitalize())
print(lenguaje.upper())
print(lenguaje.lower())
print(lenguaje.isnumeric())
print("1".isnumeric())
print(lenguaje.count("t"))
print(lenguaje.upper().isupper()) # isupper comprueba si es mayuscula
print(lenguaje.startswith("Py")) # Empieza por ...
print("Py" == "py")
