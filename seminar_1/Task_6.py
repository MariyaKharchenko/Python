REFORM = 1582
BIG_LEAP_YEAR = 400
SMALL_LEAP_YEAR = 4
LARGE_NOT_LEAP_YEAR = 100
MULTIPLE = 0

year = int(input('Введите год:'))
if year < REFORM:
    res = 'Григорианский календарь еще не существовал.'
elif year % BIG_LEAP_YEAR == MULTIPLE:
    res = f'{year} - високосный год'
elif year %  LARGE_NOT_LEAP_YEAR == MULTIPLE:
    res = f'{year} - не високосный год'
elif year % SMALL_LEAP_YEAR == MULTIPLE:
    res = f'{year} - високосный год'
else:
    res = f'{year} - не високосный год'

print(res)