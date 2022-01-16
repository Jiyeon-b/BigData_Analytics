import mglearn
from sklearn.linear_model import Ridge
from sklearn import model_selection
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

jeju=pd.read_excel('/content/sample_data/2021-11-jeju-weather.xlsx')
feature_names = ['Point', 'PointName', 'Date', 'average temperature(°C)', 'minimum temperature(°C)', 'minimum temperature time(hhmi)', 'highest temperature(°C)', 'highest temperature time(hhmi)', 'daily precipitation(mm)',
        'average wind speed(m/s)', 'average relative humidity(%)', 'average vapor pressure(hPa)', 'fermented time(hr)', 'Total daylight hours(hr)', 'solar 1 hour(hhmi)', 'solar 1 hour mount(MJ/m2)', 
        'total insolation(MJ/m2)' , 'power generation(kwh)', 'precipitation']
df = pd.DataFrame(data = jeju, columns=feature_names)

x = df[['total insolation(MJ/m2)']].values
y = df[['power generation(kwh)']].values

model = LinearRegression()

quadratic = PolynomialFeatures(degree=2)
cubic = PolynomialFeatures(degree=3)
d4 = PolynomialFeatures(degree=4)
d5 = PolynomialFeatures(degree=5)
d6 = PolynomialFeatures(degree=6)

x_quad = quadratic.fit_transform(x)
x_cubic = cubic.fit_transform(x)
x4 = d4.fit_transform(x)
x5 = d5.fit_transform(x)
x6 = d6.fit_transform(x)

x_fit = np.arange(x.min(), x.max(), 1)[:, np.newaxis]
model = model.fit(x, y)
y_fit = model.predict(x_fit)
r2 = r2_score(y, model.predict(x))

model = model.fit(x_quad, y)
y_quad_fit = model.predict(quadratic.fit_transform(x_fit))
quadratic_r2 = r2_score(y, model.predict(x_quad))

model = model.fit(x_cubic, y)
y_cubic_fit = model.predict(cubic.fit_transform(x_fit))
cubic_r2 = r2_score(y, model.predict(x_cubic))

model = model.fit(x4, y)
_y4 = model.predict(d4.fit_transform(x_fit))
_x4 = r2_score(y, model.predict(x4))

model = model.fit(x5, y)
_y5 = model.predict(d5.fit_transform(x_fit))
_x5 = r2_score(y, model.predict(x5))

model = model.fit(x6, y)
_y6 = model.predict(d6.fit_transform(x_fit))
_x6 = r2_score(y, model.predict(x6))

plt.scatter(x, y, label="Training Point", color="lightgray")
#plt.plot(x_fit, y_fit, label="linear (d=1), $R^2=%.2f$" % r2, color="blue", lw=2, linestyle=":")
#plt.plot(x_fit, y_quad_fit, label="quadratic (d=2), $R^2=%.2f$" % quadratic_r2, color="red", lw=2, linestyle="-")
#plt.plot(x_fit, y_cubic_fit, label="cubic (d=3), $R^2=%.2f$" % cubic_r2, color="green", lw=2, linestyle="--")
plt.plot(x_fit, _y4, label="(d=4), $R^2=%.2f$" % _x4, color="blue", lw=2, linestyle=":")
plt.plot(x_fit, _y5, label="(d=5), $R^2=%.2f$" % _x5, color="red", lw=2, linestyle="-")
plt.plot(x_fit, _y6, label="(d=6), $R^2=%.2f$" % _x6, color="green", lw=2, linestyle="--")
plt.xlabel("% total insolation(MJ/m2)")
plt.ylabel("power generation(kwh)")
plt.legend(loc="upper right")
plt.show()