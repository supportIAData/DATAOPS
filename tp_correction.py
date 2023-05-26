import pandas as pd
import numpy as np


names = pd.read_csv('data/names/yob1880.txt', names=['name', 'sex', 'birth'])

# 1. Nb de naissances
grouped = names.groupby('sex')['birth']

# 2. Concat yobs files
columns = ['name', 'sex', 'birth']
yobs = []

for year in range(1880, 2019):
    path = "data/names/yob{}.txt".format(year)
    df = pd.read_csv(path, names=columns)
    df['year'] = year
    yobs.append(df)

names = pd.concat(yobs, ignore_index=True)

total_births = names.pivot_table(values='birth', index='year', columns='sex', aggfunc=sum)[:10]

total_births.plot()
