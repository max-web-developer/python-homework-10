from random import randint
number_of_colomn = int(input('Введите N: '))
number_of_row = int(input('Введите M: '))
H = int(input('Введите H: '))
my_array = []
for i in range(number_of_colomn):
    temp=[]
    for j in range(number_of_row):
        n = randint(0,10) 
        temp.append(n)
    my_array.append(temp)
print(my_array)