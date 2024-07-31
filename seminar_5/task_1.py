one, two, three, *other = input('Введите строку через / ').split('/')
my_dict = {int(two): int(one), int(three): tuple(map(int, other))}

print(my_dict)