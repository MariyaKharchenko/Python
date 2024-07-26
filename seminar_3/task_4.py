data = [42, 73, 5, 42, 42, 2, 3, 5, 73, 42]

res = []

for i, item in enumerate(data, start=1):
    if item % 2:
        res.append(i)

print(res)