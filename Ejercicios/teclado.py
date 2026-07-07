### Manejo del teclado

from pynput import keyboard as teclado

def tecla_pulsa(tecla):
	print('Se ha pulsado la tecla ' + str(tecla))

def tecla_suelta(tecla):
	print('Se ha soltado la tecla ' + str(tecla))
	if tecla == teclado.KeyCode.from_char('q'):
		return False

teclado.Listener(tecla_pulsa, tecla_suelta).run()