import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the data, skipping the specific rows (2, 3, 4) but keeping the header
file_path = 'Z:/working/Training/2024-Crick Microscopy Course/Live imaging/trial data/Prelim_analysis_2/Pos7/FUCCI_LEDpower_Jul24_2_MMStack_Pos7_spots.csv'
data = pd.read_csv(file_path, skiprows=[1, 2, 3])
data.sort_values(by=['TRACK_ID', 'FRAME'], ignore_index=True, inplace=True)

# Extract necessary data
intensity_data = data[['FRAME', 'TRACK_ID', 'MEAN_INTENSITY_CH2', 'MEAN_INTENSITY_CH3']]


# Function to find the frame of a steep fall in intensity
def find_steep_fall_frame(intensity_values, threshold=0.05, window=50):
    max_fall = 0
    fall_frame = None

    for i in range(len(intensity_values) - window):
        fall = (intensity_values[i] - intensity_values[i + window]) / intensity_values[i]
        if fall > max_fall:
            max_fall = fall
            fall_frame = i

    if max_fall >= threshold:
        return fall_frame
    else:
        return None


# Calculate frame differences between intensity drops in C3 and C2
frame_differences = []

unique_tracks = intensity_data['TRACK_ID'].unique()

for track in unique_tracks:
    track_data = intensity_data[intensity_data['TRACK_ID'] == track]
    frames = track_data['FRAME'].values
    intensity_values_C2 = track_data['MEAN_INTENSITY_CH2'].values
    intensity_values_C3 = track_data['MEAN_INTENSITY_CH3'].values

    # Find the frames where steep fall occurs
    fall_frame_C3 = find_steep_fall_frame(intensity_values_C3)
    fall_frame_C2 = find_steep_fall_frame(intensity_values_C2)

    if fall_frame_C3 is not None and fall_frame_C2 is not None:
        # Calculate the difference in frames
        frame_difference = frames[fall_frame_C2] - frames[fall_frame_C3]
        if frame_difference >= 0:
            frame_differences.append(frame_difference)

# Plot the distribution of frame differences
plt.figure(figsize=(10, 6))
plt.hist(frame_differences, bins=30, range=(0, 600), color='blue', alpha=0.7, density=True)
plt.xlabel('Frame Difference (C3 drop - C2 drop)')
plt.ylabel('Number of Tracks')
plt.title('Distribution of Frame Differences between Intensity Drops in Channels 2 and 3')
plt.xlim(left=0, right=600)
plt.show()

# Optionally, print some statistics about the distribution
print(f"Mean Frame Difference: {np.mean(frame_differences):.2f}")
print(f"Median Frame Difference: {np.median(frame_differences):.2f}")
print(f"Standard Deviation of Frame Difference: {np.std(frame_differences):.2f}")
