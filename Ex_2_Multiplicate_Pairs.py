# 2 Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
n = int(input('Введите длину списка: '))
my_list = [random.randint(-10,10) for i in range(n)]
print(my_list)

import math
mult_list = []
for i in range((math.ceil(n/2))):
    mult_list.append(my_list[i]*my_list[n-1-i])
print(f'Произведение пар чисел списка равно {mult_list}')