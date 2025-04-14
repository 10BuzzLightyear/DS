#Feature Scaling and Dummification
#A. Apply feature-scaling techniqueslike standardization and normalization
#to numericalfeatures.
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler


df = pd.read_csv('wine.csv', header=None, usecols=[0, 1, 2], skiprows=1)


df.columns = ['classlabel', 'Alcohol', 'Malic Acid']


print("Original DataFrame:")
print(df)


scaling = MinMaxScaler()
scaled_value = scaling.fit_transform(df[['Alcohol', 'Malic Acid']])
df[['Alcohol', 'Malic Acid']] = scaled_value


print("\nDataFrame after MinMax Scaling:")
print(df)


scaling = StandardScaler()
scaled_standardvalue = scaling.fit_transform(df[['Alcohol', 'Malic Acid']])
df[['Alcohol', 'Malic Acid']] = scaled_standardvalue


print("\nDataFrame after Standard Scaling:")
print(df)

#B. Performfeature Dummification to convert categorical variables
#into numericalrepresentations.

import pandas as pd
from sklearn.preprocessing import LabelEncoder


iris = pd.read_csv('Iris.csv')


print(iris)


le = LabelEncoder()


iris['code'] = le.fit_transform(iris['Species'])


print(iris)
