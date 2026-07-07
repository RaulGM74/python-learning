### PROGRAMA QUE ENCRIPTA Y DESENCRIPTA UN TEXTO

clave = int(input('\nIntroduce clave (1 a 5) ..: '))
texto_origen = input('Introduce un texto .......: ')
texto_destino = ''

for caracter in texto_origen:
    caracter_en_numero = ord(caracter)
    caracter_codificado = caracter_en_numero + clave
    texto_destino = texto_destino + chr(caracter_codificado)

print(f'ENCRIPTACION .............: [{texto_origen}] --> [{texto_destino}]')