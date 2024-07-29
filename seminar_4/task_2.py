def func(text: str)->list[int]:
    result = set()
    for char in text:
        result.add(ord(char))
    return sorted(result, reverse=True)


print(func('bsfjsabhcjask'))