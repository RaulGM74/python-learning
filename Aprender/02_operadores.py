# Trabajo con operadores

# Operadores aritméticos
x = 3 * 5 - 3 + 4 / 2
print("X = ", x, " o tambien = ", 3 * 5 - 3 + 4 / 2)
print("Operador de módulo (resto de una división) = ", 11 % 2)
print("Operación aproximación a entero --> 10 // 3 =", 10 // 3)
print("Operación exponente --> 2 ** 3 =", 2 ** 3)

# Operacdores de cadenas
print("Hola " + "Python")       # Concatena cadenas
print("Hola " + str(x))         # Concatena cadenas
print("Hola " + str(int(x)))    # Concatena cadenas
print("Hi " * (2 ** 3))         # Muestra la cadena 2 elevado a 3 veces

# Operadores comparativos
print(1 > 2, 1 < 2, 1 >= 2, 1 <= 2, 1 == 2, 1 != 2) # Esto da Trues y Falses
print(1 < 2 < 3)
print("A" < "B", "A" > "B") # Compara la ordenación alfabética

# Operadores lógicos
print('1 > 2 and "A" > "B" --> ', 1 > 2 and "A" > "B")
print('not(1 > 2 and "A" > "B") --> ', not(1 > 2 and "A" > "B"))
print('1 > 2 or "A" > "B" -->', 1 > 2 or "A" > "B")
print('1 < 2 and "A" < "B" --> ', 1 < 2 and "A" < "B")


