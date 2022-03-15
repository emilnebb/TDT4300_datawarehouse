import numpy as np
from scipy.spatial import distance_matrix
import pandas as pd
import csv
from tabulate import tabulate

path = 'points_dbscan.csv'
with open(path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    headers = next(reader)
    data = np.array(list(reader)).astype(int)
data = data[:, 1:]

distance = distance_matrix(data, data)
distance = (pd.DataFrame(distance))
print(tabulate(distance,  floatfmt=".3f", headers='keys'))
