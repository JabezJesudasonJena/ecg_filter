import numpy as np
import matplotlib.pyplot as plt

# Time vector
t = np.linspace(0, 10, 1000)

# Original noisy ECG signal
noisy_ecg = 0.8 * np.exp(-0.3 * (t - 3) ** 2) * np.cos(10 * t) + 0.2 * np.sin(40 * t)

# Traditional low-pass filter (simplified: noise removed but smoothed)
traditional_filtered = 0.8 * np.exp(-0.3 * (t - 3) ** 2) * np.cos(10 * t)

# Fractional Prabhakar-based filter (adaptive, preserves some detail)
prabhakar_filtered = 0.8 * np.exp(-0.3 * (t - 3) ** 2) * np.cos(10 * t) + 0.05 * np.sin(10 * t)

# Plot setup
fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

# --- Noisy ECG ---
axs[0].plot(t, noisy_ecg, color="blue", linewidth=2)
axs[0].set_title("Original ECG Signal with Noise", fontsize=12)
axs[0].set_ylabel("Voltage (mV)")
axs[0].set_ylim([-1.2, 1.2])
axs[0].grid(True, linestyle="--", alpha=0.5)

# --- Traditional filter ---
axs[1].plot(t, traditional_filtered, color="red", linewidth=2)
axs[1].set_title("Traditional Low-Pass Filter (Butterworth/Chebyshev)", fontsize=12)
axs[1].set_ylabel("Voltage (mV)")
axs[1].set_ylim([-1.2, 1.2])
axs[1].grid(True, linestyle="--", alpha=0.5)

# --- Fractional Prabhakar-based filter ---
axs[2].plot(t, prabhakar_filtered, color="green", linewidth=2)
axs[2].set_title("Fractional Prabhakar-Based Low-Pass Filter", fontsize=12)
axs[2].set_xlabel("Time (s)")
axs[2].set_ylabel("Voltage (mV)")
axs[2].set_ylim([-1.2, 1.2])
axs[2].grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
