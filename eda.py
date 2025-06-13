import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/census.csv')
print(df.head(10))
print(df.info())
print(df.describe())
print(df.isnull().sum())