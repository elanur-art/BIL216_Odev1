import numpy as np
import matplotlib.pyplot as plt

# Frekanslar
f0 = 127
f1 = f0
f2 = f0 / 2
f3 = 10 * f0

# Örnekleme
fs = 10000
# 1/fs adımıyla zaman vektörü oluşturulur
t = np.arange(0, 0.05, 1/fs)

# Sinyaller
x1 = np.sin(2*np.pi*f1*t)
x2 = np.sin(2*np.pi*f2*t)
x3 = np.sin(2*np.pi*f3*t)
x_toplam = x1 + x2 + x3

plt.figure(figsize=(12,10))
plt.suptitle("Sinüzoidal İşaretlerin Örneklenmesi (f0 = 127 Hz)", fontsize=16)

# 1. Grafik
plt.subplot(4,1,1)
plt.plot(t, x1, color="#1f77b4", linewidth=2)
plt.title("f1 = 127 Hz")
plt.ylabel("Genlik")
plt.grid(alpha=0.3)

# 2. Grafik
plt.subplot(4,1,2)
plt.plot(t, x2, color="#2ca02c", linewidth=2)
plt.title("f2 = 63.5 Hz")
plt.ylabel("Genlik")
plt.grid(alpha=0.3)

# 3. Grafik
plt.subplot(4,1,3)
plt.plot(t, x3, color="#d62728", linewidth=2)
plt.title("f3 = 1270 Hz")
plt.ylabel("Genlik")
plt.grid(alpha=0.3)

# Toplam
plt.subplot(4,1,4)
plt.plot(t, x_toplam, color="#9467bd", linewidth=2)
plt.title("Toplam Sinyal")
plt.xlabel("Zaman (s)")
plt.ylabel("Genlik")
plt.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
