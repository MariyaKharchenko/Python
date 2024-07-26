text = input('Введите текст: ').split(' ')
text.sort()
max_len = 0
for i in text:
    current_len = len(i)
    if max_len < current_len:
        max_len = current_len

for i, item in enumerate(text, start=1):
    print(f'{i}. {item:>{max_len}}')