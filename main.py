import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
import tkinter as tk
from tkinter import ttk

def generate_wave():
    try:
        amplitude = float(amplitude_entry.get())
        frequency = float(frequency_entry.get())
        phase = float(phase_entry.get())
        wave_speed = float(wave_speed_entry.get())
        duration = float(duration_entry.get())
        sampling_rate = float(sampling_rate_entry.get())

        t = np.linspace(0, duration, int(sampling_rate * duration))

        y = amplitude * np.sin(2 * np.pi * frequency * t + phase)

        wavelength = wave_speed / frequency
        wavelength_var.set(f"{wavelength:.2f} meters")

        plt.figure(figsize=(10, 4))
        plt.subplot(1, 2, 1)
        plt.plot(t, y, color="blue")
        plt.title("Time Domain")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.grid()

        N = len(y)
        yf = fft(y)
        xf = fftfreq(N, 1 / sampling_rate)

        positive_freq_indices = xf >= 0
        xf = xf[positive_freq_indices]
        yf = 2.0 / N * np.abs(yf[positive_freq_indices])

        plt.subplot(1, 2, 2)
        plt.plot(xf, yf, color="red")
        plt.title("Frequency Domain")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.grid()

        plt.tight_layout()
        plt.show()

    except Exception as e:
        wavelength_var.set("Error occurred!")
        print(f"Error: {e}")

root = tk.Tk()
root.title("Sine Wave Generator and Analyzer")
root.geometry("500x450")
root.configure(bg="#f0f8ff")

header = tk.Label(root, text="Sine Wave Generator & Analyzer", font=("Helvetica", 16, "bold"), bg="#4682b4", fg="white")
header.pack(fill=tk.X, pady=10)

frame = ttk.Frame(root, padding=10)
frame.pack(pady=10, fill=tk.X)

fields = [
    ("Amplitude", "1"),
    ("Frequency (Hz)", "5"),
    ("Phase (radians)", "0"),
    ("Wave Speed (m/s)", "343"),
    ("Duration (s)", "1"),
    ("Sampling Rate (Hz)", "1000")
]

entries = {}

for label_text, default_value in fields:
    row = ttk.Frame(frame)
    row.pack(fill=tk.X, pady=5)
    label = ttk.Label(row, text=label_text, width=20)
    label.pack(side=tk.LEFT, padx=5)
    entry = ttk.Entry(row)
    entry.insert(0, default_value)
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    entries[label_text] = entry

amplitude_entry = entries["Amplitude"]
frequency_entry = entries["Frequency (Hz)"]
phase_entry = entries["Phase (radians)"]
wave_speed_entry = entries["Wave Speed (m/s)"]
duration_entry = entries["Duration (s)"]
sampling_rate_entry = entries["Sampling Rate (Hz)"]

wavelength_label = ttk.Label(root, text="Wavelength:", font=("Helvetica", 12, "bold"), background="#f0f8ff", foreground="#4682b4")
wavelength_label.pack(pady=5)
wavelength_var = tk.StringVar(value="Not calculated yet")
wavelength_value_label = ttk.Label(root, textvariable=wavelength_var, font=("Helvetica", 12), background="#f0f8ff", foreground="black")
wavelength_value_label.pack(pady=5)

generate_button = tk.Button(root, text="Generate & Analyze Wave", font=("Helvetica", 12, "bold"),
                            bg="#32cd32", fg="white", command=generate_wave)
generate_button.pack(pady=10)



root.mainloop()
