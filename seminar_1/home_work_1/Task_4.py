#Программа загадывает число от 0 до 1000. Необходимо угадать число
# за 10 попыток. Программа должна подсказывать “больше” или “меньше”
# после каждой попытки. Для генерации случайного числа используйте код:
#from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
attempts = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

while attempts:
    your_num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
    if your_num < num:
        print('Загаданное число больше.')
    elif your_num > num:
        print('Загаданное число меньше.')
    else:
        print('Вы угадали!')
        quit()
    attempts -= 1
print('Попытки закончились.')