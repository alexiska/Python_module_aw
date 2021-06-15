# -- 1a 
lst_student = ['James Bond','Spider Man','Donald Duck', 'Super Man', 'Bull Bear']

# -- b
print(lst_student[2])

# -- c
print(lst_student[2][0])

# -- d
lst_student[2] = 'Ole'

# -- e
lst_student[2] = lst_student[2]+" Nordmann"

#-- f
lst_student.append('Donald Duck')

#-- g
lst_student.insert(4,"Monty Python")

# -- h
print(len(lst_student))
lst_student.remove('Ole Nordmann')
print(len(lst_student))

#-- i
print(lst_student.index("Monty Python"))

# -- j
print(lst_student[:3])

#-- k
student_reverse = lst_student[::-1]

#-- l
lst_student[0::2]

#-- m
lst_student[1::2]