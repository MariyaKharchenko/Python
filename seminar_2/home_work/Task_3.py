#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем
# и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для
# проверки своего кода используйте модуль fractions

import  math
from fractions import Fraction


first_fraction = input('Введите первую дробь вида a/b: ').split('/')
second_fraction = input('Введите вторую дробь вида a/b: ').split('/')

first_numerator = int(first_fraction[0])
first_denominator = int(first_fraction[1])
second_numerator = int(second_fraction[0])
second_denominator = int(second_fraction[1])

integer = ''
sum_of_numerators = 0
denominator = 1
product_of_numerators = 0
product_of_denominators = 0

def mult (a, b):
    multiple = 0
    while multiple != 1:
        multiple = math.gcd(a, b)
        a //= multiple
        b //= multiple
        return a, b

def sum (first_numerator = first_numerator,
         first_denominator = first_denominator,
         second_numerator = second_numerator,
         second_denominator = second_denominator):

    denominator = math.lcm(first_denominator, second_denominator)
    first_numerator *= int(denominator / first_denominator)
    second_numerator *= int(denominator / second_denominator)
    sum_of_numerators = first_numerator + second_numerator

    sum_of_numerators, denominator = mult(sum_of_numerators, denominator)

    if sum_of_numerators > denominator:
        integer = sum_of_numerators // denominator
        sum_of_numerators %= denominator
        return (f'{int(first_fraction[0])}/{int(first_fraction[1])} + '
                f'{int(second_fraction[0])}/{int(second_fraction[1])} = '
                f'{integer} {sum_of_numerators}/{denominator}')
    if sum_of_numerators == denominator:
        integer = sum_of_numerators // denominator
        return (f'{int(first_fraction[0])}/{int(first_fraction[1])} + '
                f'{int(second_fraction[0])}/{int(second_fraction[1])} = '
                f'{integer}')
    return  (f'{int(first_fraction[0])}/{int(first_fraction[1])} + '
                f'{int(second_fraction[0])}/{int(second_fraction[1])} = '
                f'{sum_of_numerators}/{denominator}')


def product (first_numerator = first_numerator,
         first_denominator = first_denominator,
         second_numerator = second_numerator,
         second_denominator = second_denominator):

    product_of_numerators = first_numerator * second_numerator
    product_of_denominators = first_denominator * second_denominator
    multiple = 0

    product_of_numerators, product_of_denominators = (
        mult(product_of_numerators, product_of_denominators))

    if product_of_numerators > product_of_denominators:
        integer = product_of_numerators // product_of_denominators
        product_of_numerators %= product_of_denominators
        return (f'{int(first_fraction[0])}/{int(first_fraction[1])} * '
               f'{int(second_fraction[0])}/{int(second_fraction[1])} = '
               f'{integer} {product_of_numerators}/{product_of_denominators}')
    if product_of_numerators == product_of_denominators:
        integer = product_of_numerators // product_of_denominators
        return (f'{int(first_fraction[0])}/{int(first_fraction[1])} * '
                f'{int(second_fraction[0])}/{int(second_fraction[1])} = '
                f'{integer}')
    return (f'{int(first_fraction[0])}/{int(first_fraction[1])} * '
                f'{int(second_fraction[0])}/{int(second_fraction[1])} = '
                f'{product_of_numerators}/{product_of_denominators}')


print(sum())
print(product())

print(Fraction(first_numerator, first_denominator) + Fraction(second_numerator, second_denominator))
print(Fraction(first_numerator, first_denominator) * Fraction(second_numerator, second_denominator))
