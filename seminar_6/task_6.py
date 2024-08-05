_data = {}


def riddle(riddle_text: str, answers: list[str], count: int = 3) -> int:
    print(f'Отгадай загадку: \n{riddle_text}')
    for n in range(1, count + 1):
        ans = input(f'Попытка №{n}: ').lower()
        if ans in answers:
            return n
    return 0


def srorage():
    puzzles = {
        'Зимой и летом одним цветом': ['ель', 'елка', 'ёлка'],
        'Сидит дед, во сто шуб одет': ['лук', 'луковица'],
        'Не лает, не кусает, а в дом не пускает': ['замок', 'домофон']
    }
    for puzle, answer in puzzles.items():
        result = riddle(puzle, answer)
        print(f'Угадал с {result}й попытки' if result > 0 else 'Не угадал.')
        save_results(puzle, result)


def save_results(puzzle: str, n: int) -> None:
    _data[puzzle] = n


def show_results():
    res = (f'Загадку "{puzzle}" разгадали с {n}й попытки.' if n > 0 else
           f'Загадку "{puzzle}" не разгадали' for puzzle, n in _data.items())
    print(*res, sep='\n')

if __name__ == '__main__':
    srorage()
    show_results()