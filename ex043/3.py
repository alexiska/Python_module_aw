current_number = 40
total_numb = 100
bar_length = 10
pos = int(bar_length*(current_number/total_numb))

print("|", end="")
print("="*pos, end="")
print(">", end="")
print(" "*(bar_length-pos-1), end="")
print("|", end="")
