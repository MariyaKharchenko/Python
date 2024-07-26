text = input('Введите текст: ')
if text.isdigit():
    res = int(text)
elif (text.replace(',', '').replace('-', '').isdigit() and text.count('.') == 1
    and text.count('-') <= 1 and '-' not in text[1:]):
    res = float(text)
elif not text.islower():
    res = text.lower()
else:
    res = text.upper()


print(f'{res=}')