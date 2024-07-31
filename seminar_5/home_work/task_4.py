# Создайте функцию генератор чисел Фибоначчи.

def gen_fib(n: int):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


print(*gen_fib(10))