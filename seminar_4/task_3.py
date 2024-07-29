def func(text: str)->dict[str,int]:
    nums = list(map(int, text.split()))
    result = {chr(i): i for i in range(min(nums), max(nums) + 1)}
    return result

print(func('95 76'))