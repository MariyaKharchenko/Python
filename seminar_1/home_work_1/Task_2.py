#Треугольник существует только тогда, когда сумма любых
# двух его сторон больше третьей. Дано a, b, c - стороны
# предполагаемого треугольника. Требуется сравнить длину
# каждого отрезка-стороны с суммой двух других. Если хотя
# бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно
# сообщить является ли треугольник разносторонним, равнобедренным
# или равносторонним.

a,b,c = input('Введите 3 стороны треугольника через пробел: ').split()
a = int(a)
b = int(b)
c = int(c)

if c > a + b or a > c + b or b > a + c:
    res = 'Такого треугольника не существует'
elif a == b and a == c:
    res = 'Треугольник равносторонний'
elif a == b or a == c or b == c:
    res = 'Треугольник равнобедренный'
else:
    res = 'Треугольник разносторонний'
print(res)
