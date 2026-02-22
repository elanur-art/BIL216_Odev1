import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Temel ayarlar
fs = 8000  # Örnekleme frekansı
T = 0.3    # Sinyal süresi
N = int(fs * T)  # örnek sayısı

# DTMF frekans tablosu
dtmf_freq = {
    '1': (697, 1209), '2': (697, 1336), '3': (697, 1477), 'A': (697, 1633),
    '4': (770, 1209), '5': (770, 1336), '6': (770, 1477), 'B': (770, 1633),
    '7': (852, 1209), '8': (852, 1336), '9': (852, 1477), 'C': (852, 1633),
    '*': (941, 1209), '0': (941, 1336), '#': (941, 1477), 'D': (941, 1633)
}

# Tuş dizisi
buttons = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# DTMF sinyali üretme ve grafiği güncelleme
def play_tone(frequencies, key_name="Key"):
    t = np.linspace(0, T, N, endpoint=False)
    signal = np.sum([np.sin(2 * np.pi * f * t) for f in frequencies], axis=0)
    signal /= max(abs(signal))
    sd.play(signal, fs)

    ax_time.cla()
    ax_freq.cla()

    # Zaman grafiği
    ax_time.plot(t[:500], signal[:500])
    ax_time.set_title(f"Time Domain - {key_name}")
    ax_time.set_xlabel("Time (s)")
    ax_time.set_ylabel("Amplitude")
    ax_time.grid(True)

    # Frekans grafiği
    fft_vals = np.fft.fft(signal)
    fft_freq = np.fft.fftfreq(len(signal), 1 / fs)
    ax_freq.plot(fft_freq[:N // 2], np.abs(fft_vals[:N // 2]))
    ax_freq.set_title(f"Frequency Domain - {key_name}")
    ax_freq.set_xlabel("Frequency (Hz)")
    ax_freq.set_ylabel("Magnitude")
    ax_freq.grid(True)

    canvas.draw()

# Tkinter ana pencere
root = tk.Tk()
root.title("DTMF Generator - BIL216")
root.geometry("900x500")  # tuş takımı

frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Tuşları oluşturma
for i, row in enumerate(buttons):
    for j, key in enumerate(row):
        tk.Button(frame_left, text=key, font=("Arial", 14, "bold"),
                  command=lambda k=key: play_tone(dtmf_freq[k], f"Key {k}"),
                  width=5, height=3, relief=tk.RAISED, bg="#e0e0e0") \
            .grid(row=i, column=j, sticky="nsew", padx=5, pady=5)

# Tuş grid esnekliği
for i in range(len(buttons)):
    frame_left.grid_rowconfigure(i, weight=1)
for j in range(len(buttons[0])):
    frame_left.grid_columnconfigure(j, weight=1)

# Grafikler
fig, (ax_time, ax_freq) = plt.subplots(2, 1, figsize=(6, 4))
fig.tight_layout(pad=3)
canvas = FigureCanvasTkAgg(fig, master=frame_right)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root.mainloop()