# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def Create_Random_List(list_length):
    import random
    new_list = []
    for i in range(list_length):
        new_list.append(random.randint(-10,10))
    return new_list

n = int(input('Введите длину списка: '))
my_list = Create_Random_List(n)
print(my_list)

sum = 0
for i in range (0, n, 2):
    sum = sum + my_list[i]
print(f'Сумма чисел стоящих на нечетных позициях равна {sum}')
