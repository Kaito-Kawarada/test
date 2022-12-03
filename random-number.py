import random
import csv
import numpy as np

count = 0
list_x = []
list_y = []

while count < 500:
    numx = random.uniform(-10.0, 10.0)
    numy = random.uniform(-10.0, 10.0)
    list_x.append(numx)
    list_y.append(numy)
    count += 1

xy_array= np.array([list_x, list_y])

with open('xydata.csv', 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(xy_array)