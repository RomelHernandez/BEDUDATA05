numbers_list = [
    8,
    10,
    23,
    38,
    126,
    128,
    18,
    19,
    22,
    9,

]

def double_number(value):
    return value * 2

number = 2500
number_double=double_number(number)
print('______________________________')
print(f'Calculando el doble de {number}: {number_double}\n\n')



print('______________________________')
for n in numbers_list:
    r = double_number(n)
    print(f'Calculando el doble de {n} = {r}')



print('______________________________')
numbers_list_double = list(map(double_number, numbers_list))
print(numbers_list)
print(numbers_list_double)



print('______________________________')
double = lambda value: value * 2
print(double_number(5000))