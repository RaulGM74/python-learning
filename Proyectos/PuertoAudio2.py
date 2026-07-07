import numpy as np
import sounddevice as sd


if __name__ == "__main__":
    
    frecuencia      = 440   # Frecuencia en Hz (por ejemplo, 440 Hz es el tono A4)
    duracion        = 1     # Duración en segundos
    amplitud        = 0.5   # Amplitud del tono (entre 0.0 y 1.0)
    tasa_muestreo   = 44100 # Tasa de muestreo en Hz

    # Array NumPy con los datos del tono.        
    t = np.linspace(0, duracion, int(tasa_muestreo * duracion), endpoint=False)

    # Genera un tono sinusoidal.
    tono1 = amplitud * np.sin(2 * np.pi * frecuencia * t)

    # Emite un tono por el puerto de salida de audio.
    #   :frecuencia : Frecuencia del tono en Hz.
    #   :duracion   : Duración del tono en segundos.
    sd.play(tono1, samplerate=tasa_muestreo)  # Reproduce el tono
    sd.wait() # Espera a que se complete la reproducción del tono

