# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

data = (r'C:\user\docs\Letter.txt').split('\\')


def parse_path(data: str):
    *path, name = data
    extension = ''
    path = '/'.join(path)

    i = -1
    while name[i] != '.':
        extension = name[i] + extension
        name = name[:-1]
    name = name[:-1]

    return (path, name, extension)


print(parse_path(data))