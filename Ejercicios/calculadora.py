### CALCULADORA
### Programa que hace de calculadora

# Funciones
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

print("\n")
print("\n")

while True:
    
    # Menú principal
    print("\n Por favor, elige una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("0. Terminar")

    # Solicitar al usuario que ingrese la opción
    opcion = input("Ingresa una opción (1/2/3/4/0): ")

    if opcion >= '1' and opcion <= '4':
        # Solicitar al usuario que ingrese los números
        num1 = float(input("Primer número  : "))
        num2 = float(input("Segundo número : "))

    # Realizar la operación seleccionada
    if opcion == '1':
        print('Resultado: ', num1, "+", num2, "=", suma(num1, num2))

    elif opcion == '2':
        print('Resultado: ', num1, "-", num2, "=", resta(num1, num2))


    elif opcion == '3':
        print('Resultado: ', num1, "*", num2, "=", multiplicacion(num1, num2))

    elif opcion == '4':
        print('Resultado: ', num1, "/", num2, "=", division(num1, num2))

    elif opcion == '0':
        print('\nHasta pronto')
        break
    else:
        print("Opción inválida")