def func(names:list[str], salary:list[int], bonus:list[str]) -> dict[str, float]:
    result = {name: salary * float(bonus[:-1]) / 100
              for name, salary, bonus in zip(names, salary, bonus)}
    return result


n = ['Иван', 'Николай', 'Григорий']
s = [125_000, 97_000, 118_000]
a = ['10%', '25.5%', '15%']

print(func(n, s, a))