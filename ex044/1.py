#### -- a -- ###
num1 = float(input('First value: '))
num2 = float(input('Second value: '))
operator = input("Operator: ")

if operator == '+':
    res = num1 + num2
elif operator == '-':
    res = num1 - num2
elif operator == '*':
    res = num1 * num2
else:
    res = num1 / num2

print('The result is ',res)


#### -- b -- ###

num1 = (input('First value: '))
if num1.isalpha():
    print('First value should be numeric!')
    num1 = float(input('First value: '))
else:
    num1 = float(num1)
    
num2 = (input('Second value: '))
if num2.isalpha():
    print('Second value should be numeric!')
    num2 = float(input('Second value: '))
else:
    num2 = float(num2)
    
operator = input("Operator: ")
if operator not in ['+','-','*','/']:
    print('Valid operators are: +,-,*, or /')
    operator = input("Operator: ")
    
if operator == '+':
    res = num1 + num2
elif operator == '-':
    res = num1 - num2
elif operator == '*':
    res = num1 * num2
else:
    res = num1 / num2

print('The result is ',res)

#### -- c -- ###
num1 = (input('First value: '))
if num1.isalpha():
    print('First value should be numeric!')
    num1 = float(input('First value: '))
else:
    num1 = float(num1)
    
num2 = (input('Second value: '))
if num2.isalpha():
    print('Second value should be numeric!')
    num2 = float(input('Second value: '))
else:
    num2 = float(num2)
    
operator = input("Operator: ")
if operator not in ['+','-','*','/']:
    print('Valid operators are: +,-,*, or /')
    operator = input("Operator: ")
    

if operator == '+':
    res = num1 + num2
    print('The result is ',res)
elif operator == '-':
    res = num1 - num2
    print('The result is ',res)
elif operator == '*':
    res = num1 * num2
    print('The result is ',res)
else:
    if num2 == 0:
        print("Cannot divide with zero!")
    else:
        res = num1 / num2
        print('The result is ',res)


