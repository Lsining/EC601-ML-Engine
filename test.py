#%matplotlib inline

import pandas as pd
import numpy as np
from pandas import DataFrame
import datetime
import pandas.io.data
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('test.csv', index_col='business_id')
#print df.head(20)

df2 = df[['name', 'stars', 'review_count', 'full_address', 'city', 'state', 'latitude', 'longitude','categories']]
df3 = df2[['stars']]
df4 = df2[['review_count']]

threedee = plt.figure().gca(projection='3d')
threedee.scatter(df2.index, df2['stars'], df2['review_count'])
threedee.set_xlabel('business_id')
threedee.set_ylabel('stars')
threedee.set_zlabel('review_count')

print df2.dtypes
#print (df2.head(10))

#df2.to_csv('test2.csv')

#df2[['city', 'review_count']].plot(kind='scatter', x='df3', y='df4')
#df2.plot()
plt.show()
