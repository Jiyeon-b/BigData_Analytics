import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
plt.style.use('fivethirtyeight')
import warnings

warnings.filterwarnings('ignore')
%matplotlib inline

data=pd.read_excel('/content/sample_data/2021-11-jeju-weather.xlsx')

data[['Total daylight hours(hr)', 'power generation(kwh)']].groupby(['Total daylight hours(hr)'], as_index=True).mean().sort_values(by='power generation(kwh)',ascending=False).plot.bar()
