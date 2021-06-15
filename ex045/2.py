import random

dice = [1,2,3,4,5,6]
n_dices = 5

# -- a 
rand_dices = random.choices(dice, k=n_dices)
print(rand_dices)

# -- b
if (rand_dices[0] == rand_dices[1] and
   rand_dices[1] == rand_dices[2] and
    rand_dices[2] == rand_dices[3] and
    rand_dices[3] == rand_dices[4]):
        print("Yahtzee!")
else:
    print("No Yahtzee =(")
    
# -- c
print(f"Max value: {max(rand_dices)} and Min value: {min(rand_dices)}")
print("sorted list: ", sorted(rand_dices))