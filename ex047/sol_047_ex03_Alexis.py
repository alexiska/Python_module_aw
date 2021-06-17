def my_calculator(num1,num2,operator):
    
    if operator == '+':
        res = num1 + num2
    elif operator == '-':
        res = num1 - num2
    elif operator == '*':
        res = num1 * num2
    else:
        res = num1 / num2
    return res 
        
num1 = float(input('First value: '))
num2 = float(input('Second value: '))
operator = input("Operator: ")

result = my_calculator(num1,num2,operator)

print('The result is ',result)

