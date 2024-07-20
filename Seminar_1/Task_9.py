LOWER_LIMIT = 2
UPPER_LIMIT = 10
COLUMN = 4
ONE = 1

for i_main in (LOWER_LIMIT, LOWER_LIMIT + COLUMN):
    for second_num in range(LOWER_LIMIT, UPPER_LIMIT + ONE):
        for first_num in range(i_main, COLUMN + i_main):
            print(f'{first_num:>2} x {second_num:>2} = {first_num * second_num:>2}', end='\t')
        print()
    print()