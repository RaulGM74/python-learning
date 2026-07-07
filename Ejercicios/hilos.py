### Hilos

import time
from threading import Thread

def funcion1(parametro1):
    for i in range(10):
        time.sleep(1)
        print(parametro1)

hilo1 = Thread(target=funcion1, args=('Hola hilo 1',))
hilo2 = Thread(target=funcion1, args=('Hola hilo 2',))
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()
print("Fin hilos.")