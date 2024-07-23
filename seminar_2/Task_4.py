import math
import decimal

decimal.getcontext().prec = 50
PI = decimal.Decimal(math.pi)

d = decimal.Decimal(input('Введите диаметр окружности: '))

while d > 1000:
    print('Некорректный ввод.')
    d = decimal.Decimal(input('Введите диаметр окружности: '))
print(f'Площадь круга = {PI * (d / 2)**2}, \n Длина окружности = {PI * d}')