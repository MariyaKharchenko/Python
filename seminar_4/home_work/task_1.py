# Напишите функцию для транспонирования матрицы


our_matrix = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]

for i in  our_matrix:
    print(f'{i}')


def func(lst:list[list[int]]) -> list[list[int]]:
    result = []
    if len(lst) >= len(lst[0]):
        for i in range(len(lst)):
            res = []
            for row in lst:
                res.append(row[i])
            result.append(res)
    else:
        for i in range(len(lst[0])):
            res = []
            for row in lst:
                res.append(row[i])
            result.append(res)
    return result


new_matrix = func(our_matrix)
print()



new_matrix = func(our_matrix)

for i in  new_matrix:
    print(f'{i}')