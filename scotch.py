##################################################

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

scotch_df = pd.read_csv('Scotch.csv')

scotch_df = scotch_df.join(pd.get_dummies(scotch_df['DISTRICT']))
print scotch_df.head(10)
