import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')
sns.set(font_scale=2.5)
import missingno as msno

import warnings
warnings.filterwarnings('ignore')

%matplotlib inline
 
import matplotlib as mpl
import matplotlib.font_manager as fm

mpl.rcParams['axes.unicode_minus'] = False
plt.rcParams["figure.figsize"] = (20,10)

plt.rc('font', family='NanumGothic')
plt.rc('font', size=8)        # 기본 폰트 크기
plt.rc('axes', labelsize=8)   # x,y축 label 폰트 크기
plt.rc('xtick', labelsize=8)  # x축 눈금 폰트 크기 
plt.rc('ytick', labelsize=8)  # y축 눈금 폰트 크기
plt.rc('legend', fontsize=8)  # 범례 폰트 크기
plt.rc('figure', titlesize=8) # figure title 폰트 크기
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams.update({'font.size' : 8})

from sklearn.datasets import load_boston

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')
sns.set(font_scale=2.5)
import missingno as msno

import warnings
warnings.filterwarnings('ignore')

%matplotlib inline
 
import matplotlib as mpl
import matplotlib.font_manager as fm

mpl.rcParams['axes.unicode_minus'] = False
plt.rcParams["figure.figsize"] = (20,10)

plt.rc('font', family='NanumGothic')
plt.rc('font', size=8)        # 기본 폰트 크기
plt.rc('axes', labelsize=8)   # x,y축 label 폰트 크기
plt.rc('xtick', labelsize=8)  # x축 눈금 폰트 크기 
plt.rc('ytick', labelsize=8)  # y축 눈금 폰트 크기
plt.rc('legend', fontsize=8)  # 범례 폰트 크기
plt.rc('figure', titlesize=8) # figure title 폰트 크기
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams.update({'font.size' : 8})

from sklearn.datasets import load_boston

jeju=pd.read_excel('/content/sample_data/2021-11-jeju-weather.xlsx')
df = pd.DataFrame(data = jeju, columns=feature_names)

cols = [ 'average temperature(°C)', 'average relative humidity(%)', 'Total daylight hours(hr)', 'solar 1 hour(hhmi)','total insolation(MJ/m2)' , 'power generation(kwh)', 'precipitation']
sns.pairplot(df[cols])
plt.show()