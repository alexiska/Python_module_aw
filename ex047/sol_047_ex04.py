import math
# --a--
def throw_distance(velocity, angle, init_height=1.8):
    
    alpha = math.radians(angle)
    throw_velocity = velocity/3.6
    vh = throw_velocity*math.cos(alpha)
    vv = throw_velocity*math.sin(alpha)
    g = 9.81
    t = (vv+math.sqrt(vv**2+2*g*init_height))/g
    R = vh * t

    print(f"Throw angel in radians [alpha]: {alpha:.2f}")
    print(f"Throw velocity in m/s [v_0]: {throw_velocity:.2f}")
    print(f"Throw velocity in the horizontal direction [v_x]: {vh:.2f}")
    print(f"Throw velocity in the vertical direction [v_y]: {vv:.2f}")
    print(f"Airtime [t]: {t:.2f}")
    print(f"Throw distance [R]: {R:.2f}") 


throw_distance(50,45) #for testing if the fkn works 

# --b--
def kmh_to_ms(velocity):
    return velocity/3.6

def throw_distance(velocity, angle, init_height=1.8):
    
    alpha = math.radians(angle)
    throw_velocity = kmh_to_ms(velocity) 
    vh = throw_velocity*math.cos(alpha)
    vv = throw_velocity*math.sin(alpha)
    g = 9.81
    t = (vv+math.sqrt(vv**2+2*g*init_height))/g
    R = vh * t

    print(f"Throw angel in radians [alpha]: {alpha:.2f}")
    print(f"Throw velocity in m/s [v_0]: {throw_velocity:.2f}")
    print(f"Throw velocity in the horizontal direction [v_x]: {vh:.2f}")
    print(f"Throw velocity in the vertical direction [v_y]: {vv:.2f}")
    print(f"Airtime [t]: {t:.2f}")
    print(f"Throw distance [R]: {R:.2f}") 

throw_distance(50,45)  

# -- c --
def kmh_to_ms(velocity):
    return velocity/3.6

def velocity_decomposition(velocity,alpha):
    vh = velocity*math.cos(alpha)
    vv = velocity*math.sin(alpha)
    return [vh,vv]

def throw_distance(velocity, angle, init_height=1.8):
    
    alpha = math.radians(angle)
    throw_velocity = kmh_to_ms(velocity) 
    vh, vv = velocity_decomposition(throw_velocity, alpha)
    
    g = 9.81
    t = (vv+math.sqrt(vv**2+2*g*init_height))/g
    R = vh * t

    print("Throw angel in radians [alpha]: ", round(alpha,2))
    print("Throw velocity in m/s [v_0]:", round(throw_velocity,2))
    print("Throw velocity in the horizontal direction [v_x]: ",round(vh,2))
    print("Throw velocity in the vertical direction [v_y]: ", round(vv,2))
    print("Airtime [t]: ",round(t,2))
    print("Throw distance [R]: ",round(R,2)) 


throw_distance(50,45)

# -- d --
def kmh_to_ms(velocity):
    return velocity/3.6

def velocity_decomposition(velocity,alpha):
    vh = velocity*math.cos(alpha)
    vv = velocity*math.sin(alpha)
    return [vh,vv]

def airtime(vv, init_height, g=9.81):
    t = (vv+math.sqrt(vv**2+2*g*init_height))/g
    return t

def throw_distance(velocity, angle, init_height=1.8):
    
    alpha = math.radians(angle)
    throw_velocity = kmh_to_ms(velocity) 
    vh, vv = velocity_decomposition(throw_velocity, alpha)
    t = airtime(vv, init_height, g=9.81)
    R = vh * t

    print("Throw angel in radians [alpha]: ", round(alpha,2))
    print("Throw velocity in m/s [v_0]:", round(throw_velocity,2))
    print("Throw velocity in the horizontal direction [v_x]: ",round(vh,2))
    print("Throw velocity in the vertical direction [v_y]: ", round(vv,2))
    print("Airtime [t]: ",round(t,2))
    print("Throw distance [R]: ",round(R,2)) 


throw_distance(50,45)

# -- e --