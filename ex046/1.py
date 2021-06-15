# -- a --
var_1, var_2 , var_3 = 1 ,2 ,3

# -- b --
temp = var_1
var_1 = var_2
var_2 = temp
print("var_1: ", var_1)
print("var_2: ", var_2)

# -- c --
var_1, var_2 , var_3 = 1 ,2 ,3
var_1, var_2 = var_2, var_1
print("var_1: ", var_1)
print("var_2: ", var_2)