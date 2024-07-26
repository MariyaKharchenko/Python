data = [42, 73, 5, 42, 42, 2, 3, 5, 73, 42]
COUNT_DOUBLE = 2

for i in set(data):
    if data.count(i) == COUNT_DOUBLE:
        for _ in range(COUNT_DOUBLE):
            data.remove(i)

print(data)