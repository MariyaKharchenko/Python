data = {
    'Рога': [42, -73, 12, 85, -15, 2],
    'Копыта': [45, 25, 100, 22, 1],
    'Хвосты': [500, 123, 52, 45, 93]
}

def func(data: dict[str, list[int]]):
    return  len(list(filter(lambda x: sum(x) > 0, data.values()))) == len(data)

print(func(data))