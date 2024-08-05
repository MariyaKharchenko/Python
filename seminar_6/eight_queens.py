"""
Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях. Известно,
что на доске 8×8 можно расставить 8 ферзей так, чтобы они
не били друг друга. Вам дана расстановка 8 ферзей на доске,
oпределите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число
от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг
друга верните истину, а если бьют - ложь.
Напишите функцию в шахматный модуль. Используйте генератор
случайных чисел для случайной расстановки ферзей в задаче
выше. Проверяйте различный случайные варианты и выведите
4 успешных расстановки.
"""
from random import choice


QUEENS = 8
x_list = [0, 1, 2, 3, 4, 5, 6, 7]
y_list = [0, 1, 2, 3, 4, 5, 6, 7]
MAX_COUNT = 4


def line_up():
    """
    Эта функция расставляет ферзей на доске так,
    чтобы их координаты не совпадали.
    Возвращает список с координатами каждого ферзя.
    """
    queens_on_the_board = []
    count = 0
    while count < QUEENS:
        i = choice(x_list)
        j = choice(y_list)
        if [i, j] not in queens_on_the_board:
            queens_on_the_board.append([i, j])
            count += 1
    return queens_on_the_board


queens_on_the_board = line_up()


def check_the_arrangement(queens_on_the_board = queens_on_the_board) -> bool:
    """
    Эта функция получает на вход список с координатами каждого ферзя и
    проверяет бьют ли ферзи друг друга, возвращая True, если не бьют,
    возвращая False в случае, если ферзи бьют друг друга.
    """
    x = []
    y = []

    for i in range(QUEENS):
        x.append(queens_on_the_board[i][0])
        y.append(queens_on_the_board[i][1])
    for i in range(QUEENS):
        for j in range(i + 1, QUEENS):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
    return True



def print_luck():
    """
    Эта функция возвращает MAX_COUNT успешных расстановок ферзей.
    """
    count = 0
    while count < MAX_COUNT:
        queens_on_the_board = line_up()
        if check_the_arrangement(queens_on_the_board) == True:
            print(queens_on_the_board)
            count += 1
        else:
            queens_on_the_board.clear()


if __name__ == '__main__':
    queens_on_the_board = [[7, 5], [1, 1], [6, 3], [2, 4], [3, 2], [5, 6], [0, 7], [4, 0]]
    print(f'Если ферзи не бьют друг друга: {check_the_arrangement(queens_on_the_board)}')
    queens_on_the_board = [[3, 1], [3, 3], [4, 5], [1, 4], [5, 2], [5, 7], [7, 7], [2, 6]]
    print(f'Если ферзи бьют друг друга: {check_the_arrangement(queens_on_the_board)}')
    print_luck()

    """
    Вывод функции print_luck:
    [[1, 6], [6, 3], [7, 7], [2, 1], [5, 0], [0, 4], [4, 2], [3, 5]]
    [[1, 0], [3, 5], [4, 2], [0, 4], [7, 3], [2, 7], [5, 6], [6, 1]]
    [[2, 2], [5, 7], [4, 5], [7, 3], [0, 6], [3, 0], [6, 1], [1, 4]]
    [[7, 0], [1, 1], [6, 4], [5, 7], [3, 2], [4, 5], [0, 3], [2, 6]]
    """


