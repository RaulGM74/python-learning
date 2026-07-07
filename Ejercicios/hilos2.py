# Hios / https://www.codigopiton.com/como-usar-hilos-o-threads-en-python/

import threading

def ejecutar(parametro1=10, parametro2=20):
    print('Hilo:', threading.current_thread().name, '   / ID: ', threading.get_native_id(), ' / Parm1: ', parametro1, ' / Parm2: ', parametro2)

def info():
    print('Hilo:', threading.current_thread().name, '   / ID: ', threading.get_native_id())

# creamos los hilos
hilo1 = threading.Thread(target=info)
hilo2 = threading.Thread(target=info)
hilo3 = threading.Thread(target=info)
hilo10 = threading.Thread(target=ejecutar)
hilo20 = threading.Thread(target=ejecutar, args=(100, 200))
hilo30 = threading.Thread(target=ejecutar, kwargs={'parametro1': 1000, 'parametro2': 2000})
hilo40 = threading.Thread(target=ejecutar, args=(300, 400), name='HiloRGM')

# ejecutamos los hilos
hilo1.start()
hilo2.start()
hilo3.start()
hilo10.start()
hilo20.start()
hilo30.start()
hilo40.start()

# el programa principal sigue ejecutándose aunque los hilos no hayan terminado
print('Hilo:', threading.current_thread().name, '   / ID: ', threading.get_native_id())
