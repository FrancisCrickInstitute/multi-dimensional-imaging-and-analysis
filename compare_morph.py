import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file_path_0 = 'Z:/working/Training/2024-Crick Microscopy Course/Live imaging/trial data/Preliminary_Analysis/FUCCI_LEDpower_Jul24_1_MMStack_Pos0_spots.csv'
data0 = pd.read_csv(file_path_0, skiprows=[1, 2, 3])
data0['POSITION'] = 0
file_path_7 = 'Z:/working/Training/2024-Crick Microscopy Course/Live imaging/trial data/Preliminary_Analysis/FUCCI_LEDpower_Jul24_1_MMStack_Pos7_spots.csv'
data7 = pd.read_csv(file_path_7, skiprows=[1, 2, 3])
data7['POSITION'] = 7

morph_data = pd.DataFrame();

frames = pd.unique(data0['FRAME'])

for f in frames:
    frame_data0 = data0[data0['FRAME'] == f]
    frame_data7 = data7[data7['FRAME'] == f]
    mean_area0 = np.mean(frame_data0['AREA'])
    sd_area0 = np.std(frame_data0['AREA'])
    mean_area7 = np.mean(frame_data7['AREA'])
    sd_area7 = np.std(frame_data7['AREA'])
    mean_circ0 = np.mean(frame_data0['CIRCULARITY'])
    sd_circ0 = np.std(frame_data0['CIRCULARITY'])
    mean_circ7 = np.mean(frame_data7['CIRCULARITY'])
    sd_circ7 = np.std(frame_data7['CIRCULARITY'])
    morph_data = pd.concat([morph_data,
                            pd.DataFrame(data=[[f, mean_area0, mean_circ0, 0], [f, mean_area7, mean_circ7, 7]],
                                         columns=['FRAME', 'AREA', 'CIRCULARITY', 'POSITION'])])

plt.figure(figsize=(6.0, 5.0), dpi=300)
plt.scatter(morph_data[morph_data['POSITION'] == 0]['FRAME'], morph_data[morph_data['POSITION'] == 0]['AREA'],
            alpha=0.7,
            label='Pos0')
plt.scatter(morph_data[morph_data['POSITION'] == 7]['FRAME'], morph_data[morph_data['POSITION'] == 7]['AREA'],
            alpha=0.7,
            label='Pos7')
plt.legend()
plt.show()

plt.figure(figsize=(6.0, 5.0), dpi=300)
plt.scatter(morph_data[morph_data['POSITION'] == 0]['FRAME'], morph_data[morph_data['POSITION'] == 0]['CIRCULARITY'],
            alpha=0.7,
            label='Pos0')
plt.scatter(morph_data[morph_data['POSITION'] == 7]['FRAME'], morph_data[morph_data['POSITION'] == 7]['CIRCULARITY'],
            alpha=0.7,
            label='Pos7')
plt.legend()
plt.show()
