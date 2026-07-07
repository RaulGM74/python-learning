import os

################################################################################
## Función: Recorre un directorio y muestra los archivos con su ruta completa.
################################################################################
def listar_archivos(directorio):
    for carpeta, subcarpetas, archivos in os.walk(directorio):
        for archivo in archivos:
            ruta_completa = os.path.join(carpeta, archivo)
            print(ruta_completa, '-->', archivo)


################################################################################
## INICIO PROGRAMA
################################################################################
print("\nRGM. Inicio Programa\n")

# Cambia esta ruta por el directorio que quieres recorrer
directorio = '/Users/midr/Movies/ProcesoExif'
# listar_archivos(directorio)

for carpeta, subcarpetas, archivos in os.walk(directorio):
    for archivo in archivos:
        FechaCorrecta = f"{archivo[0:4]}:{archivo[5:7]}:{archivo[8:10]} {archivo[11:13]}:{archivo[13:15]}:00+01:00"
        print(archivo, '->',FechaCorrecta)
        # Modificar metadato FileModifyDate del archivo con el valor de FechaCorrecta
        os.system(f'exiftool -FileModifyDate="{FechaCorrecta}" "{os.path.join(carpeta, archivo)}"')
        # os.system(f'exiftool -FileAccessDate="{FechaCorrecta}" "{os.path.join(carpeta, archivo)}"')
        # os.system(f'exiftool -FileInodeChangeDate="{FechaCorrecta}" "{os.path.join(carpeta, archivo)}"')
        os.system(f'exiftool -CreateDate="{FechaCorrecta}" "{os.path.join(carpeta, archivo)}"')
        os.system(f'exiftool -ModifyDate="{FechaCorrecta}" "{os.path.join(carpeta, archivo)}"')
        # os.system(f'exiftool -TrackCreateDate="{FechaCorrecta}" "{os.path.join(carpeta, archivo)}"')
        # os.system(f'exiftool -TrackModifyDate="{FechaCorrecta}" "{os.path.join(carpeta, archivo)}"')
        # os.system(f'exiftool -MediaCreateDate="{FechaCorrecta}" "{os.path.join(carpeta, archivo)}"')
        # os.system(f'exiftool -MediaModifyDate="{FechaCorrecta}" "{os.path.join(carpeta, archivo)}"')

print("\nRGM. Fin Programa\n")
################################################################################
## FIN PROGRAMA
################################################################################