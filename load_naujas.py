import pandas as pd
import numpy as np

# Load dirty data
df = pd.read_csv('naujas.csv', encoding='latin1',  parse_dates=[0])

# Rename columns
df.index.name = 'N'
df.rename(columns = {'2015Startas:Laik': 'Laik'}, inplace = True)

# Clean date column
for name in ['Laik']:
    df[name] = pd.to_datetime(df[name], errors='coerce', format="%y-%m-%d %H:%M:%S")

# Clean numeric columns
for name in ['It', 'Sr', 'Temp', 'Galia', 'Apkr %', 'Kor', 'Vejo gr', 'Turbinos RPM']:
    df[name] = pd.to_numeric(df[name], errors='coerce')

# Drop invalid rows
df.dropna(axis=0, inplace=True)

# Save cleaned data
df.to_csv('naujas_clean.csv')
