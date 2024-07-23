import sys

data = [42, 73.0, 'hello', 42, 2**8]
print
for i, j in enumerate(data, 1):
    check_int = 'Похоже на целое число' if isinstance(j, int) else ''
    check_str = 'Похоже на строку' if isinstance(j, str) else ''
    print(f'{i}. Объект {j}. Адрес в памяти {id(j)}. Размер в памяти {sys.getsizeof(j)}. Хэш {hash(j)}. {check_str} {check_int}')