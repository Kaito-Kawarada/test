import csv
import numpy as np
import pandas as pd

count = 0
xy_dataframe = pd.read_csv("xydata.csv", header=None)
xy_array = pd.DataFrame.to_numpy(xy_dataframe)

r = np.sqrt(xy_array[:,0] ** 2 + xy_array[:,1] ** 2).reshape(-1, 1)
theta = np.degrees(np.arctan2(xy_array[:,0], xy_array[:,1])).reshape(-1, 1)

print(xy_array.shape)
print(r.shape)

xy_array = np.hstack((xy_array, r))
xy_array = np.hstack((xy_array, theta))
#np.hstack(xy_array,theta)

xy_dataframe = pd.DataFrame(xy_array)
xy_dataframe.to_csv('xydata2.csv', index=False, header=False)