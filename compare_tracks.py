import matplotlib.pyplot as plt
import pandas as pd

file_path_0 = 'Z:/working/Training/2024-Crick Microscopy Course/Live imaging/trial data/Prelim_analysis_2/Pos0/FUCCI_LEDpower_Jul24_2_MMStack_Pos0_tracks.csv'
data0 = pd.read_csv(file_path_0, skiprows=[1, 2, 3])
data0['POSITION'] = 0
file_path_7 = 'Z:/working/Training/2024-Crick Microscopy Course/Live imaging/trial data/Prelim_analysis_2/Pos7/FUCCI_LEDpower_Jul24_2_MMStack_Pos7_tracks.csv'
data7 = pd.read_csv(file_path_7, skiprows=[1, 2, 3])
data7['POSITION'] = 7

speed_data = pd.concat([data0[['TRACK_MEAN_SPEED', 'POSITION']], data7[['TRACK_MEAN_SPEED', 'POSITION']]])

plt.figure(figsize=(6.0, 5.0), dpi=300)
plt.hist(data0['TRACK_MEAN_SPEED'], bins=20, alpha=0.7, label='Pos0', histtype='barstacked')
plt.hist(data7['TRACK_MEAN_SPEED'], bins=20, alpha=0.7, label='Pos7', histtype='barstacked')
plt.xlabel("Mean Cell Velocity (\u03BCm/s)")
plt.ylabel("Number of Cells")
plt.legend()
plt.show()
