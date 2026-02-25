import numpy as np
from scipy.io import wavfile
import os


def add_white_noise(input_path, output_path, noise_level=0.02):
    """
    Dodaje biały szum do pliku WAV i zapisuje wynik jako nowy plik.
    
    :param input_path: ścieżka do pliku wejściowego .wav
    :param output_path: ścieżka do pliku wyjściowego .wav
    :param noise_level: poziom szumu (np. 0.01 - 0.05 rozsądny zakres)
    """
    
    # Wczytaj plik
    sample_rate, data = wavfile.read(input_path)
    
    # Konwersja do float (jeśli dane są int)
    if data.dtype != np.float32:
        max_val = np.iinfo(data.dtype).max
        data = data.astype(np.float32) / max_val

    # Generowanie białego szumu
    noise = np.random.normal(0, 1, data.shape)
    
    # Dodanie szumu
    noisy_data = data + noise_level * noise
    
    # Ograniczenie zakresu do [-1, 1]
    noisy_data = np.clip(noisy_data, -1.0, 1.0)
    
    # Konwersja z powrotem do int16
    noisy_data_int = (noisy_data * 32767).astype(np.int16)
    
    # Zapis pliku
    wavfile.write(output_path, sample_rate, noisy_data_int)
    
    print(f"Zapisano plik z szumem jako: {output_path}")


if __name__ == "__main__":
    input_wav = r"R:\studia\Gniadek\zaj1\advanced_techniques\Zaj1\tone_440.wav"
    
    # Tworzy nazwę kopii automatycznie
    base, ext = os.path.splitext(input_wav)
    output_wav = f"{base}_noisy{ext}"
    
    add_white_noise(input_wav, output_wav, noise_level=0.05)