import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

# Load the data
file_path = 'C:/Users/davej/Downloads/FUCCI_LEDpower_Jul24_1_MMStack_spots.csv'
data = pd.read_csv(file_path)

# Extract the necessary data
intensity_data = data[['FRAME', 'TRACK_ID', 'MEAN_INTENSITY_CH2', 'MEAN_INTENSITY_CH3']]


# Function to find the point of steep fall in intensity
def find_steep_fall(intensity_values, threshold=0.1, window=10):
    for i in range(len(intensity_values) - window):
        if (intensity_values[i] > 0 and (intensity_values[i] - intensity_values[i + window]) / intensity_values[i]
                >= threshold):
            return i
    return None


# Align intensity data based on the steep fall
def align_intensity_data(data, channel_fall, channel_intensity):
    aligned_data = []
    unique_tracks = data['TRACK_ID'].unique()

    for track in unique_tracks:
        track_data = data[data['TRACK_ID'] == track]
        intensity_values_fall = track_data[channel_fall].values
        intensity_values_intensity = track_data[channel_intensity].values

        fall_point = find_steep_fall(intensity_values_fall)

        if fall_point is not None:
            aligned_intensity = intensity_values_intensity[fall_point:]
            aligned_data.append(aligned_intensity)

    # Pad shorter arrays with NaNs to create a rectangular array
    max_length = max(len(arr) for arr in aligned_data)
    aligned_data = [np.pad(arr, (0, max_length - len(arr)), 'constant', constant_values=np.nan) for arr in aligned_data]

    # Convert to a DataFrame
    aligned_df = pd.DataFrame(aligned_data).T
    return aligned_df


# Align and average intensity for each channel
aligned_intensity_CH2 = align_intensity_data(intensity_data, 'MEAN_INTENSITY_CH2', 'MEAN_INTENSITY_CH2')
aligned_intensity_CH3 = align_intensity_data(intensity_data, 'MEAN_INTENSITY_CH2', 'MEAN_INTENSITY_CH3')

# Calculate the mean intensity across all tracks
mean_aligned_intensity_CH2 = aligned_intensity_CH2.mean(axis=1)
mean_aligned_intensity_CH3 = aligned_intensity_CH3.mean(axis=1)

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(mean_aligned_intensity_CH2.index, mean_aligned_intensity_CH2.values, label='Geminin-mCherry (C2)', color='red')
plt.plot(mean_aligned_intensity_CH3.index, mean_aligned_intensity_CH3.values, label='Cdt-Venus (C3)', color='green')
plt.xlabel('Aligned Time (Frame)')
plt.ylabel('Mean Intensity')
plt.title('Aligned Mean Fluorescence Intensity Over Time for FUCCI')
plt.legend()
plt.grid(True)
plt.show()

# Plot intensity profiles of a few randomly selected TRACK_IDs before alignment
num_samples = 1  # Number of tracks to plot
random_tracks = random.sample(list(intensity_data['TRACK_ID'].unique()), num_samples)

plt.figure(figsize=(12, 6))
for track in random_tracks:
    track_data = intensity_data[intensity_data['TRACK_ID'] == track]
    plt.scatter(track_data['FRAME'], track_data['MEAN_INTENSITY_CH2'], label=f'TRACK_ID {track} - C2', alpha=0.7)
    plt.scatter(track_data['FRAME'], track_data['MEAN_INTENSITY_CH3'], label=f'TRACK_ID {track} - C3', alpha=0.7)

plt.xlabel('Frame')
plt.ylabel('Intensity')
plt.title('Fluorescence Intensity Profiles of Randomly Selected TRACK_IDs Before Alignment')
plt.legend()
plt.grid(True)
plt.show()

# Plot intensity profiles of the same randomly selected TRACK_IDs post alignment
plt.figure(figsize=(12, 6))
for track in random_tracks:
    if track in aligned_intensity_CH2.columns:
        plt.scatter(aligned_intensity_CH2.index, aligned_intensity_CH2[track], label=f'TRACK_ID {track} - C2', alpha=0.7)
        plt.scatter(aligned_intensity_CH3.index, aligned_intensity_CH3[track], label=f'TRACK_ID {track} - C3', alpha=0.7)

plt.xlabel('Aligned Time (Frame)')
plt.ylabel('Intensity')
plt.title('Fluorescence Intensity Profiles of Randomly Selected TRACK_IDs Post Alignment')
plt.legend()
plt.grid(True)
plt.show()