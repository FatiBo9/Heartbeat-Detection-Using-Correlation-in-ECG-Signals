import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import neurokit2 as nk

#generating a synthetic ECG signal using NeuroKit2 a biblio which is easy 
#to analyze biological signals
frequency = 300         #sampling rate 
duration = 13
ecg_signal = nk.ecg_simulate(duration=duration, sampling_rate=frequency)
time_array = np.linspace(0, duration, len(ecg_signal))
plt.figure(figsize=(12, 4))
plt.plot(time_array, ecg_signal)
plt.title("my signal ecg using NeuroKit2")
plt.xlabel("time (s)")
plt.ylabel("amplitude")
plt.grid(True)
plt.show()

#Extracting a segment of the ECG signal that represents a single heartbeat
_, ecg_output = nk.ecg_peaks(ecg_signal, sampling_rate=frequency)
r_peaks = ecg_output["ECG_R_Peaks"]
#choosing the first peak 
first_r_peak = r_peaks[0]
#setting a window around the beat
before = int(0.3 * frequency)  
after = int(0.4 * frequency)   
beat_segment = ecg_signal[first_r_peak - before : first_r_peak + after]
time_segment = np.linspace(-0.3, 0.4, len(beat_segment))
#this part it detects the locations of heartbeats (R peaks) in the ECG signal, 
#selects the first heartbeat then calculates a time window before and after this beat
#extracts that part of the ECG signal around the beat and creates a matching time axis to analyze the heartbeat shape
plt.figure(figsize=(10, 4))
plt.plot(time_segment, beat_segment)
plt.title("Template: oneheartbeat")
plt.xlabel("time (s)")
plt.ylabel("amplitude")
plt.grid(True)
plt.show()

#normalization:
def normalize_signal(signal):
    return (signal - np.min(signal)) / (np.max(signal) - np.min(signal)) * 2 - 1
#normalization of my signal ecg 
ecg_signal_normalized = normalize_signal(ecg_signal)
#normalization of my template (segment)
template_normalized = normalize_signal(beat_segment)
plt.figure(figsize=(12, 4))
plt.plot(ecg_signal_normalized, label="my ecg signal normalized")
plt.plot(np.arange(first_r_peak - before, first_r_peak + after), template_normalized, color='green', label="template_normalized")
plt.legend()
plt.title("my signal ecg and template normalized")
plt.grid(True)
plt.show()

#computing the Cross-Correlation using scipy.signal.correlate
cross_correlation = signal.correlate(ecg_signal_normalized, template_normalized, mode='valid')
#finding the index where the template best matches the ECG signal, 
#this corresponds to the highest peak in the cross-correlation 
max_correlation= np.argmax(cross_correlation)
plt.figure(figsize=(12, 4))
plt.plot(ecg_signal_normalized, label="my ecg signal normalized")
plt.plot(np.arange(max_correlation, max_correlation + len(template_normalized)), 
         template_normalized, color='r', label="my template correlated")
plt.title("the cross-correlation between the template (single heartbeat) and the entire ECG signal")
plt.legend()
plt.grid(True)
plt.show()

#Analyzing the cross-correlation output to identify peaks that correspond 
#to occurrences of the heartbeat template within the ECG signal:
threshold = 0.6 * np.max(cross_correlation)
distance_min = int(0.6 * frequency)
peaks, _ = signal.find_peaks(cross_correlation, height=threshold, distance=distance_min) 
plt.figure(figsize=(12, 4))
plt.plot(cross_correlation, label="cross-correlation")
plt.plot(peaks, cross_correlation[peaks], marker='*', color='purple',linestyle='None', label="identified peaks")
plt.title("identifying peaks in cross-correlation")
plt.legend()
plt.grid(True)
plt.show()

#Impact of Noise on Detection
#Adding noise
noise_amplitude = 0.9 
noisy_ecg = ecg_signal + np.random.normal(0, noise_amplitude, size=len(ecg_signal))
plt.figure(figsize=(12, 4))
plt.plot(time_array, noisy_ecg, label="my ecg signal with noise")
plt.title("signal ecg with noise")
plt.xlabel("time (s)")
plt.ylabel("amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#normalization of the noisy signal
noisy_ecg_normalized = normalize_signal(noisy_ecg)
#cross-correlation 
cross_correlation_noisy = signal.correlate(noisy_ecg_normalized, template_normalized, mode='valid')
#identifying peaks in noisy correlation 
noisy_threshold = 0.6 * np.max(cross_correlation_noisy)
peaks_noisy, _ = signal.find_peaks(cross_correlation_noisy, height=noisy_threshold, distance=distance_min)
correlation_shift = len(template_normalized) // 2
peaks_noisy_aligned = peaks_noisy + correlation_shift
plt.figure(figsize=(12, 4))
plt.plot(cross_correlation_noisy, label="cross-correlation with noisy signal")
plt.plot(peaks_noisy, cross_correlation_noisy[peaks_noisy], marker='*', color='purple',linestyle='None', label="identifying peaks")
plt.title("cross-correlation with noisy signal")
plt.xlabel("samples")
plt.ylabel("amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

