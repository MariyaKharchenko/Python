#Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление. Функцию hex
# используйте для проверки своего результата.

BASE = 16

num = int(input('Введите целое число: '))
base_str: str = '0123456789abcdef'
res = ''
new_num: int = num

while new_num > BASE:
    res = base_str[new_num % BASE] + res
    new_num //= BASE
new_num = base_str[new_num] + res

print(f'В шестнадцатиричной системе исчисления число {num} - это 0x{new_num}')

print(hex(num))