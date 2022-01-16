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

fig, ax = plt.subplots(1, 1, figsize=(9,5))
sns.kdeplot(data[data['precipitation'] == 1]['power generation(kwh)'], ax=ax)
sns.kdeplot(data[data['precipitation'] == 0]['power generation(kwh)'], ax=ax)
plt.legend(['precipitation == 1', 'precipitation == 0'])
plt.show()