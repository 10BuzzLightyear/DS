#Data Frames and Basic Data Pre-processing
#ARead data from CSV and JSON files into a 

import pandas as pd


df = pd.read_csv(r'C:\Users\avina\OneDrive\Desktop\DS\Student_Marks.csv')

print("Our dataset:")
print(df)


import pandas as pd


data = pd.read_json('data.json')

print(data)

#B. Perform basic data pre-processing tasks such as handling missing values
# Replacing NA values using 
import pandas as pd


df = pd.read_csv('titanic.csv')

print(df)


print(df.head(10))


print("Dataset after filling NA values with 0:")
df2 = df.fillna(value=0)


print(df2)

# Dropping NA values using

import pandas as pd


df = pd.read_csv('titanic.csv')

print(df)


print(df.head(10))


print("Dataset after dropping NA values:")
df.dropna(inplace=True)


print(df)

#C. Manipulate and transform data using functions like filtering, sorting,

import pandas as pd


iris = pd.read_csv('Iris.csv')


setosa = iris[iris['Species'] == 'setosa']
print("Setosa samples:")
print(setosa.head())


sorted_iris = iris.sort_values(by='SepalLengthCm', ascending=False)
print("\nSorted iris dataset:")
print(sorted_iris.head())


grouped_species = iris.groupby('Species').mean()
print("\nMean measurements for each species:")
print(grouped_species)



