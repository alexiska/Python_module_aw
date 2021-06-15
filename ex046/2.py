# -- a --
captured = ('Pikachu', 'Pidgey', 'Abra', 'Pidgey', 'Eevee', 'Pidgey') # Tuple

# -- b --
# list is should be more favorable coz you can add more pokemons later while with tuple i can't

# -- c --
print("Number of Pidgeys: ",captured.count('Pidgey'))

# -- d --
pokemon = input('Pokemon name: ')
if pokemon in captured:
    print('Exist')
else:
    print('Does not Exist') 
print(f"Number of unique pokemon you have is: {set(captured).__len__()}")