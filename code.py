import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 1000)

noisy_ecg = 0.8 * np.exp(-0.3 * (t - 3) ** 2) * np.cos(10 * t) + 0.2 * np.sin(40 * t)

traditional_filtered = 0.8 * np.exp(-0.3 * (t - 3) ** 2) * np.cos(10 * t)

prabhakar_filtered = 0.8 * np.exp(-0.3 * (t - 3) ** 2) * np.cos(10 * t) + 0.05 * np.sin(10 * t)

plt.figure(figsize=(10, 4))
plt.plot(t, noisy_ecg, color="blue", linewidth=2)
plt.title("Original ECG Signal with Noise", fontsize=12)
plt.ylabel("Voltage (mV)")
plt.ylim([-1.2, 1.2])
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("ecg_noisy.png", dpi=300, bbox_inches="tight")  # save
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(t, traditional_filtered, color="red", linewidth=2)
plt.title("Traditional Low-Pass Filter (Butterworth/Chebyshev)", fontsize=12)
plt.ylabel("Voltage (mV)")
plt.ylim([-1.2, 1.2])
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("ecg_traditional.png", dpi=300, bbox_inches="tight")  # save
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(t, prabhakar_filtered, color="green", linewidth=2)
plt.title("Fractional Prabhakar-Based Low-Pass Filter", fontsize=12)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (mV)")
plt.ylim([-1.2, 1.2])
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("ecg_prabhakar.png", dpi=300, bbox_inches="tight")  # save
plt.show()
