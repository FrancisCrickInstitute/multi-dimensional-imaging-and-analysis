import random

import matplotlib.pyplot as plt
import pandas as pd

# Load the data
file_path = 'Z:/working/Training/2024-Crick Microscopy Course/Live imaging/trial data/Prelim_analysis_2/Pos0/FUCCI_LEDpower_Jul24_2_MMStack_Pos0_spots.csv'
data = pd.read_csv(file_path, skiprows=[1, 2, 3])
data.sort_values(by=['TRACK_ID', 'FRAME'], ignore_index=True, inplace=True)

# Extract the necessary data
intensity_data = data[['FRAME', 'TRACK_ID', 'MEAN_INTENSITY_CH2', 'MEAN_INTENSITY_CH3']]

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
