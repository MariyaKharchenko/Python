from task_4 import *


def srorage():
    puzzles = {
        'Зимой и летом одним цветом': ['ель', 'елка', 'ёлка'],
        'Сидит дед, во сто шуб одет': ['лук', 'луковица'],
        'Не лает, не кусает, а в дом не пускает': ['замок', 'домофон']
    }
    for puzle, answer in puzzles.items():
        result = riddle(puzle, answer)
        print(f'Угадал с {result}й попытки' if result > 0 else 'Не угадал.')


if __name__ == '__main__':
    srorage()