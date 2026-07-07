### Control del ratón. Bastante completo

from pynput import mouse
import time

# el controlador de movimiento del mouse pasará las coordenadas del espacio de la pantalla a las que
# se ha movido el mouse, puede notar que todas las devoluciones de llamada del mouse le darán la
# posición del mouse.
def on_mouse_move(mouse_position_x, mouse_position_y):
  print("El ratón se ha movido a (%s, %s)"%(mouse_position_x, mouse_position_y))

# entonces la devolución de llamada de desplazamiento del mouse le dará 2 conjuntos de cambios de
# desplazamiento, uno para el eje x y otro para el y. La mayoría de las veces lo que te importa es
# el cambio del eje y.
def on_mouse_scroll(mouse_position_x, mouse_position_y, scroll_x_change, scroll_y_change):
  if scroll_x_change < 0:
    print("El usuario se desplaza hacia la izquierda")
  elif scroll_x_change > 0:
    print("El usuario se desplaza hacia la derecha")
  if scroll_y_change > 0:
    print("El usuario se desplaza hacia arriba en la página")
  elif scroll_y_change < 0:
    print("El usuario se desplaza hacia abajo en la página")
    print("scroll change deltas: ", scroll_x_change, scroll_y_change)

# la devolución de llamada al hacer clic con el mouse le indicará el botón presionado y su estado,
# la devolución de llamada se activará una vez cuando se presione el botón y nuevamente cuando se
# suelte, is_pressed le dirá en qué estado se encuentra, hay varios tipos de botones que puede
# reconocer, pero en su mayor parte solo necesitarás los 3 principales: izquierda, derecha y medio
def on_mouse_click(mouse_position_x, mouse_position_y, button, is_pressed):
  # ejemplo de como escuchar un botón específico
  if button == mouse.Button.middle and is_pressed:
    print("Botón del medio")
  else:
    print("Botón presionado: ", button)
    print("¿El botón está presionado?: ", is_pressed)

# crear un listener y establecer llamadas
mouse_listener = mouse.Listener(
                                on_move=on_mouse_move,
                                on_scroll=on_mouse_scroll,
                                on_click=on_mouse_click
                                )

# iniciar listern del mouse
print("Iniciando listener del ratón, estará activo durante 5 segundo...")
mouse_listener.start()

# let the main thread sleep for 5 seconds, then stop the listener
time.sleep(5)
print("Se acabó el tiempo, deteniendo listener del ratón")
mouse_listener.stop()
mouse_listener.join()