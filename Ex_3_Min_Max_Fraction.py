# 3 Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
n = int(input('Введите длину списка: '))
my_list = [round(random.uniform(-10,10),2) for i in range(n)]
print(my_list)

fract_list = []
for i in range(n):
    fract_list.append(round(abs(my_list[i])%1,2))
# print(fract_list)

print(f'Разница между максимальным и минимальным значением дробной части элементов равна {round(max(fract_list)-min(fract_list),2)}')