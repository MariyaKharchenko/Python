from random import randint


def guess(lower: int = 0, upper: int = 100, count: int = 10) -> bool:
    num = randint(lower, upper)
    for n in range(1, count + 1):
        answer = int(input(f'Попытка №{n}, введите число между {lower} и {upper}: '))
        if num < answer:
            print(f'Число {answer} больше загаданного.')
        elif num > answer:
            print(f'Число {answer} меньше загаданного.')
        else:
            return True
    return False


if __name__ == '__main__':
    print(guess())