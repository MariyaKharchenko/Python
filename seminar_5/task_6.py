LOWER_LIMIT = 2
UPPER_LIMIT = 10
COLUMN = 4
ONE = 1

table_gen = (f'{f_num:>2} X {s_num:>2} = {f_num*s_num:>2}\t'
             if f_num < i_man + COLUMN - ONE else
             f'{f_num:>2} X {s_num:>2} = {f_num*s_num:>2}\n'
             if s_num < UPPER_LIMIT else
             f'{f_num:>2} X {s_num:>2} = {f_num*s_num:>2}\n\n'
             for i_man in (LOWER_LIMIT, LOWER_LIMIT + COLUMN)
             for s_num in range(LOWER_LIMIT, UPPER_LIMIT + ONE)
             for f_num in range(i_man, i_man + COLUMN))

print(*table_gen)

