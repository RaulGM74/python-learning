import numpy as np
import sounddevice as sd

def generar_tono(frecuencia, duracion, amplitud=0.5, tasa_muestreo=44100):
    """
    Función que genera un tono sinusoidal.
        :frecuencia : Frecuencia del tono en Hz.
        :duracion   : Duración del tono en segundos.
        :amplitud   : Amplitud del tono (entre 0.0 y 1.0).
        :tasa_muestreo: Tasa de muestreo en Hz.
        :return     : Array NumPy con los datos del tono.
    """
    t = np.linspace(0, duracion, int(tasa_muestreo * duracion), endpoint=False)
    np.lines
    tono = amplitud * np.sin(2 * np.pi * frecuencia * t)
    return tono

def emitir_tono(frecuencia, duracion):
    """
    Función que emite un tono por el puerto de salida de audio.
        :frecuencia : Frecuencia del tono en Hz.
        :duracion   : Duración del tono en segundos.
    """
    tono = generar_tono(frecuencia, duracion)
    sd.play(tono, samplerate=44100)
    sd.wait()

if __name__ == "__main__":
    frecuencia = 440  # Frecuencia en Hz (por ejemplo, 440 Hz es el tono A4)
    duracion = 1      # Duración en segundos
    emitir_tono(frecuencia, duracion)