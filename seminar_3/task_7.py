text = 'kafhskjhbcskjchbsj'
res = {}

for char in set(text):
    res[char] = text.count(char)
print(f'{res = }')

res_2 = {}
for char in text:
    if char in res_2:
        res_2[char] += 1
    else:
        res_2[char] = 1
    #res_2[char] = res_2.get(char, 0) + 1
print(f'{res_2 = }')