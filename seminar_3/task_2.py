data = (42, 73, 3.14, 'Hello world', None, True, 'Text', 100500.2, False)
result = {}

for i in data:
    key = type(i)
    if key not in result:
        value = [x for x in data if isinstance(x, type(i))]
        result[key] = value
print(f'{result=}')