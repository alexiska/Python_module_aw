import random 

# -- a
# creating random number with list comprehension
values = [int(random.random()*10) for i in range(15)]
alpha = 0.5

# -- b
sorted_values = sorted(values)
sorted_values

# -- c
n = len(sorted_values)
lower_idx = round(n*alpha/2)
upper_idx = round(n*(1-alpha/2))-1

# -- d
print("Lower: ",sorted_values[lower_idx])
print("Upper: ",sorted_values[upper_idx])

