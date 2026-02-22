import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import tkinter as tk

# -------------------------------
# Sistem Parametreleri
# -------------------------------

fs = 8000          # Örnekleme frekansı (Hz)
T = 0.3            # Sinyal süresi (saniye)
N = int(fs * T)    # Örnek sayısı

# -------------------------------
# DTMF Frekans Tablosu
# -------------------------------

dtmf_freq = {
    '1': (697, 1209),
    '2': (697, 1336),
    '3': (697, 1477),
    'A': (697, 1633),
    '4': (770, 1209),
    '5': (770, 1336),
    '6': (770, 1477),
    'B': (770, 1633),
    '7': (852, 1209),
    '8': (852, 1336),
    '9': (852, 1477),
    'C': (852, 1633),
    '*': (941, 1209),
    '0': (941, 1336),
    '#': (941, 1477),
    'D': (941, 1633)
}

# -------------------------------
# DTMF Sinyali Üretme Fonksiyonu
# -------------------------------

def generate_tone(key):
    f_low, f_high = dtmf_freq[key]

    # Zaman vektörü
    t = np.linspace(0, T, N, endpoint=False)

    # İki frekansın üretilmesi
    signal = np.sin(2 * np.pi * f_low * t) + \
             np.sin(2 * np.pi * f_high * t)

    # Normalizasyon (Clipping önleme)
    signal = signal / 2

    # -------------------------------
    # Ses Çalma
    # -------------------------------
    sd.play(signal, fs)

    # -------------------------------
    # Zaman Domain Grafiği
    # -------------------------------
    plt.figure(figsize=(12,4))

    plt.subplot(1,2,1)
    plt.plot(t[:500], signal[:500])
    plt.title(f"Time Domain - Key {key}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()

    # -------------------------------
    # FFT (Frekans Domain Analizi)
    # -------------------------------
    fft_vals = np.fft.fft(signal)
    fft_freq = np.fft.fftfreq(len(signal), 1/fs)

    plt.subplot(1,2,2)
    plt.plot(fft_freq[:N//2],
             np.abs(fft_vals[:N//2]))
    plt.title("Frequency Domain (FFT)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()

    plt.tight_layout()
    plt.show()


# -------------------------------
# GUI Tasarımı
# -------------------------------

root = tk.Tk()
root.title("DTMF Generator - BIL216")

buttons = [
    ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['*','0','#','D']
]

for i, row in enumerate(buttons):
    for j, key in enumerate(row):
        tk.Button(root,
                  text=key,
                  width=6,
                  height=3,
                  command=lambda k=key: generate_tone(k)
                  ).grid(row=i, column=j)

root.mainloop()
