import numpy as np
from scipy import stats

n = 1000
angle = stats.norm.rvs(loc=48, scale=7, size=n)
v = stats.weibull_max.rvs(2,loc=107, scale=4, size=n)
height = 2

alpha = np.radians(angle)
throw_velocity = v/3.6
vh = throw_velocity*np.cos(alpha)
vv = throw_velocity*np.sin(alpha)
g = 9.81
t = (vv+np.sqrt(vv**2+2*g*height))/g
R = vh * t

print("Throw distance [R]: ",R.round(2)) 