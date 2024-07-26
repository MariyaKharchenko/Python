SPACE = ' '
STAR = '*'
ONE = 1
rows = int(input('Введите кол-во рядов: '))
spaces = rows - ONE
stars = ONE
for i in range(rows):
    print(spaces * SPACE + stars * STAR)
    spaces -= ONE
    stars += ONE + ONE
