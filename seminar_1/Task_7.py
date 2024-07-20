LOWER_LIMIT = 1
UPPER_LIMIT = 999
ONE = 1
TEN = 10
HUNDRED = 100
SQUARE = 2

num = 0
while num < LOWER_LIMIT or num > UPPER_LIMIT:
    num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}:'))
if num < TEN:
    res = f'Число {num} - цифра. Её квадрат равен {num**SQUARE}.'
elif num < HUNDRED:
    first_num = num//TEN
    second_num = num%TEN
    res = f'Число {num} - двухзначное число. Произведение цифр = {first_num*second_num}.'
else:
    first_num = num//HUNDRED
    second_num = num//TEN%TEN
    third_num = num%TEN
    mirror = third_num * HUNDRED + second_num * TEN + first_num
    res = f'Число {num} - трехзначное число. Его зеркальное число = {mirror}.'
print(res)