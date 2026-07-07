## Programa para leer puerto USB

# Abrir el puerto USB
import serial
import time
import os
import sys
import datetime

# Definir la función para leer el puerto USB
def leer_puerto_usb(puerto):
    try:
        # Configurar el puerto serie
        ser = serial.Serial(puerto, 9600, timeout=1)

        time.sleep(2)  # Esperar a que se establezca la conexión

        # Leer datos del puerto serie
        while True:
            if ser.in_waiting > 0:
                linea = ser.readline().decode('utf-8').rstrip()
                print(f"Datos recibidos: {linea}")
                # Aquí puedes agregar el código para procesar los datos recibidos

    except serial.SerialException as e:
        print(f"Error al abrir el puerto [{puerto}]: [{e}]")
    except KeyboardInterrupt:
        print("Interrupción del usuario. Cerrando el programa.")
    finally:
        ser.close()  # Cerrar el puerto serie al finalizar


# PROGRAMA PRINCIPAL

# Definir el puerto USB a leer
puerto_usb = '/dev/ttyUSB0'  # Cambia esto según tu sistema operativo
# puerto_usb = 'COM3'  # Cambia esto según tu sistema operativo

# Llamar a la función para leer el puerto USB
leer_puerto_usb(puerto_usb)
