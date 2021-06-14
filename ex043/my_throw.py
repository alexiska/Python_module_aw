import math
angle = float(input('Angle: '))
v = float(input('Velocity: '))
height = float(input('Height: '))

# i
alpha = math.radians(angle)

# ii
throw_velocity = v/3.6

# iii
vh = throw_velocity*math.cos(alpha)

# iv
vv = throw_velocity*math.sin(alpha)

# v
g = 9.81
t = (vv+math.sqrt(vv**2+2*g*height))/g

# vi
R = vh * t

# d & e
print(f"Throw angel in radians [alpha]: {alpha:.2f}")
print(f"Throw velocity in m/s [v_0]: {throw_velocity:.2f}")
print(f"Throw velocity in the horizontal direction [v_x]: {vh:.2f}")
print(f"Throw velocity in the vertical direction [v_y]: {vv:.2f}")
print(f"Airtime [t]: {t:.2f}")
print(f"Throw distance [R]: {R:.2f}") 


# f

# angle = 45
# v = 50
# height = 2

# # i
# alpha = math.radians(angle)

# # ii
# throw_velocity = v/3.6

# # iii
# vh = throw_velocity*math.cos(alpha)

# # iv
# vv = throw_velocity*math.sin(alpha)

# # v
# g = 9.81
# t = (vv+math.sqrt(vv**2+2*g*height))/g

# # vi
# R = vh * t

# # d & e
# print(f"Throw angel in radians [alpha]: {alpha:.2f}")
# print(f"Throw velocity in m/s [v_0]: {throw_velocity:.2f}")
# print(f"Throw velocity in the horizontal direction [v_x]: {vh:.2f}")
# print(f"Throw velocity in the vertical direction [v_y]: {vv:.2f}")
# print(f"Airtime [t]: {t:.2f}")
# print(f"Throw distance [R]: {R:.2f}") 