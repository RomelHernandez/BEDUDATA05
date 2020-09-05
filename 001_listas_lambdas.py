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
print('_________________________')
print(f'Calculando el doble de {number}: {number_double}\n\n')


print('_________________________')
for n in numbers_list:
    r = double_number(n)
    print(f'Calculando el doble de {n} = {r}')