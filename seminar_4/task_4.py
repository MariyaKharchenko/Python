def func(lst:list[int]) -> list[int]:
    cnt = 1
    while cnt < len(lst):
        is_sorted = True
        for i in range(len(lst) - cnt):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                is_sorted = False
        if is_sorted:
            break
        cnt += 1
    return lst


lst_sorted = [42, 5, 53, 74, 87, 116, 0]
func(lst_sorted)
print(func(lst_sorted))
