evens = (num for num in range(0, 100, 2) if (num % 10)+(num // 10) != 8)
print(*evens, sep='\n')