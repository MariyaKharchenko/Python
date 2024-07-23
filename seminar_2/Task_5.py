a = float(input('Введите коэффициент а = '))
b = float(input('Введите коэффициент b = '))
c = float(input('Введите коэффициент c = '))

d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    result = f'У уравнения 2 корня: {x1=}, {x2=}'
elif d == 0:
    x = -b / (2 * a)
else:
    d = complex(d, 0)
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    result = f'У уравнения 2 комплексных корня: x1 = {round(x1.real, 2) + round(x1.imag, 2)* 1j}, x2 = {round(x2.real), 2 + round(x2.imag, 2)* 1j}'
print(result)