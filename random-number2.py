import csv
import numpy as np
import pandas as pd

low, high = -10, 10
xy_array = np.random.rand(500,2)
xy_array = (high - low) * xy_array + low

xy_dataframe = pd.DataFrame(xy_array)
xy_dataframe.to_csv('xydata.csv', index=False, header=False)