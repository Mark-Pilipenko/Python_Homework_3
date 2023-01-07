# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

decimal_number = int(input('Введите целое число: '))
binary_number = str(bin(decimal_number))
binary_number = int(binary_number.lstrip('0b'))
print(f'Число {decimal_number} в двоичной системе счисления: {binary_number}')