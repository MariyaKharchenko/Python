datas = [42, -73, 12, 85, -15, 2]
s = 'Hello world'
names = ('NoName', 'OtherName', 'NewName')
sx = 42

def func():
    data = globals().copy()
    for var, value in data.items():
        if var.endswith('s') and len(var) > 1:
            globals()[var[:-1]] = value
            globals()[var] = None


func()
print(f'{datas = }')
print(f'{s = }')
print(f'{names = }')
print(f'{sx = }')
print(f'{data = }')
print(f'{name = }')
