import numpy as np


angles = np.array([10,45,60])
v = np.array([50,30,20])
height = 2

alpha = np.radians(angles)
throw_velocity = v/3.6
vh = throw_velocity*np.cos(alpha)
vv = throw_velocity*np.sin(alpha)
g = 9.81
t = (vv+np.sqrt(vv**2+2*g*height))/g
R = vh * t

print("Throw angel in radians [alpha]: ", alpha.round(2))
print("Throw velocity in m/s [v_0]:", throw_velocity.round(2))
print("Throw velocity in the horizontal direction [v_x]: ", vh.round(2))
print("Throw velocity in the vertical direction [v_y]: ", vv.round(2))
print("Airtime [t]: ",t.round(2))
print("Throw distance [R]: ",R.round(2)) 

