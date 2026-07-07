import time
import serial

# Configuración del puerto USB
# Cambia 'COM3' por el nombre del puerto USB correspondiente en tu sistema
# y ajusta la velocidad de baudios si es necesario.
puerto_usb = '/dev/ttyUSB0'  # Ejemplo para Linux/MacOS
velocidad_baudios = 9600

try:
    # Abre el puerto USB
    with serial.Serial(puerto_usb, velocidad_baudios, timeout=1) as puerto:
        # Secuencia de datos a enviar
        secuencia = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        
        for dato in secuencia:
            # Escribe el dato en el puerto USB
            puerto.write(f"{dato}\n".encode())
            print(f"Enviado: {dato}")
            # Espera 1 segundo antes de enviar el siguiente dato
            time.sleep(1)

except serial.SerialException as e:
    print(f"Error al acceder al puerto USB: {e}")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")