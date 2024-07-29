def func(nums:list[int], first:int, second:int):
    min_i = max(min(first, second), 0)
    max_i = min(max(first, second), len(nums))
    result = sum(nums[min_i:max_i])
    return result


print(func([1, 3, 15, 20, 27], 0, 10))