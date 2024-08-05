def riddle(riddle_text: str, answers: list[str], count: int = 3) -> int:
    print(f'Отгадай загадку: \n{riddle_text}')
    for n in range(1, count + 1):
        ans = input(f'Попытка №{n}: ').lower()
        if ans in answers:
            return n
    return 0


if __name__ == '__main__':
    result = riddle('Зимой и летом одним цветом', ['ель', 'ёлка', 'елка'])
    print(f'Угадал с {result}й попытки' if result > 0 else 'Не угадал.')