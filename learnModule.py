import arithmatic as a  # our custom module imported from same directory

# print(a.add(2,3))
# print(a.sub(2,3))

import math as m

# print(m.ceil(2.3))
# print(m.floor(2.3))
# print(m.factorial(5))
# print(m.sqrt(16))

import random as rand

# rand.seed(10)
# print(int(rand.randrange(1, 6)))

students = ['komal', 'ankita', 'mrudugandha', 'sakshi', 'shruti', 'mamta', 'naima', 'sakshi', 'mansi']
stud1 = []
stud2 = []
# print(rand.sample(students,1))

currentlist=True
for x in range(len(students)):

    stud = rand.sample(students, 1)
    if True:
        stud1 = stud
    else:
        stud2=stud
    currentlist=not currentlist
    students.remove(stud[0])
    # print(students)
print(stud1)
print(stud2)
