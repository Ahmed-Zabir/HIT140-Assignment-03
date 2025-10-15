import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np


df1 = pd.read_csv('/content/dataset1(HIT140).csv')
df2 = pd.read_csv('/content/dataset2(HIT140).csv')

df1['season'] = df1['season'].map({0: 'Winter', 1: 'Spring'})

df2['season'] = df2['month'].map({0:'Winter', 1:'Winter', 2:'Winter',
                                  3:'Spring', 4:'Spring', 5:'Spring', 6:'Spring'})


df1['bat_landing_to_food'] = pd.to_numeric(df1['bat_landing_to_food'], errors='coerce')
df2['bat_landing_number'] = pd.to_numeric(df2['bat_landing_number'], errors='coerce')
df2['rat_minutes'] = pd.to_numeric(df2['rat_minutes'], errors='coerce')

df1 = df1.dropna(subset=['bat_landing_to_food', 'season', 'risk'])
df2 = df2.dropna(subset=['bat_landing_number', 'rat_minutes', 'season'])