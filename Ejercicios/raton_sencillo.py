### Control del Ratón

from pynput import mouse

mouse_pressed = dict.fromkeys((mouse.Button.left, mouse.Button.right, mouse.Button.unknown), False)

def OnClick(x, y, button, pressed):
    mouse_pressed[button]=pressed

mouse.Listener(on_click=OnClick).start()
        
while True:
    if(mouse_pressed[mouse.Button.left]):
        print("boton izquierdo presionado")
        break
    if(mouse_pressed[mouse.Button.right]):
        print("boton derecho presionado")
        break