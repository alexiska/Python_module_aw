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

sample_mean = np.mean(R)
SEM = sem(R) # sample error of mean. Standard deviation divided by the square root of the sample size.
CI_95 = 1.96 * stats.sem(R) # 1.96 is the standard deviation for 95%CI
sample_low = sample_mean - CI_95 # Lower boundary in 95%CI
sample_up = sample_mean + CI_95 # Upper boundary in 95%CI
print("sample_lower: ", round(sample_low,2))
print("sample_mean: ", round(sample_mean,2))
print("sample_higher: ", round(sample_up,2))