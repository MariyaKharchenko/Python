fizzbuzz_gen = ('FizzBuzz' if num % 15 == 0 else
                'Fizz' if num % 3 == 0 else
                'Buzz' if num % 5 == 0 else num
                for num in range(1, 101))

print(*fizzbuzz_gen)