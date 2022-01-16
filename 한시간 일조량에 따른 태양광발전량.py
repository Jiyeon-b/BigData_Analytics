import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
plt.style.use('fivethirtyeight')
import warnings
import matplotlib.font_manager as font_manager
import matplotlib as mpl

warnings.filterwarnings('ignore')
%matplotlib inline

data=pd.read_excel('/content/sample_data/2021-11-jeju-weather.xlsx')

ratio = []
for i in range(1,12):
  ratio.append(
      data[data['Total daylight hours(hr)'] < i]['power generation(kwh)'].sum()
      / len(data[data['Total daylight hours(hr)'] < i]['power generation(kwh)'])
  )
plt.figure(figsize=(7,7))
plt.plot(ratio)
plt.title('Solar power generation according to one hour of sunlight', y=1.02)
plt.ylabel('power generation(kwh)')
plt.xlabel('Total daylight hours range')
plt.show()
