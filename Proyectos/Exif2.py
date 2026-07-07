import os
import subprocess

################################################################################
## INICIO PROGRAMA
################################################################################
print("\nRGM. Inicio Programa\n")

# Cambia esta ruta por el directorio que quieres recorrer
directorio = '/Users/midr/Movies/ProcesoExif'
# listar_archivos(directorio)

for carpeta, subcarpetas, archivos in os.walk(directorio):
    for archivo in archivos:
        cmd = f'exiftool -CreateDate "{os.path.join(carpeta, archivo)}"'
        print(cmd)
        result = subprocess.getoutput(cmd)
        print(archivo, '-->', f"{result}")


print("\nRGM. Fin Programa\n")
################################################################################
## FIN PROGRAMA
################################################################################