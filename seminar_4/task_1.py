def func(text: str) -> None:
    result = sorted(text.split())
    max_len = len(max(result, key=len))
    for i, item in enumerate(result, 1):
        print(f'{i} {item:>{max_len}}')


func('три девицы под окном пряли поздно вечерком')