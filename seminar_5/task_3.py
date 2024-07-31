text = 'Три девицы под окном пряли поздно вечерком.'
my_dict = {i: ord(i) for i in set(text)}

my_dict_iter = iter(my_dict.items())

for i in range(5):
    print(*next(my_dict_iter))