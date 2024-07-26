hike = {
    'Aaz' : ('спички', 'спальник', 'дрова', 'топор'),
    'Skeeve' : ('спальник', 'спички', 'вода', 'еда'),
    'Tananda' : ('вода', 'спички', 'косметичка')
 }

all_thinks = set()

for values in hike.values():
    all_thinks.update(values)

print(f'{all_thinks}')


things_all_friends = list(hike.values())
things_first_friends = things_all_friends[0]
things_other_friends = things_all_friends[1:]

for thing in things_first_friends:
    all_friends = True
    for things in things_other_friends:
        if thing not in things:
            all_friends = False
    if all_friends:
        print(f'Вещь {thing} есть у всех друзей.')

unique = {}

for master_key, master_value in hike.items():
    for slave_key, slave_value in hike.items():
        if master_key != slave_key:
            if not unique.get(master_key):
                unique[master_key] = set(master_value) - set(slave_value)
            else:
                unique[master_key] -= set(slave_value)

print(unique)


dublikates = all_thinks

for things in unique.values():
    dublikates -= things
print(f'{dublikates=}')

for key, value in hike.items():
    result = dublikates-set(value)
    if result:
        print(f'У {key} отсутсвуют следующие вещи: {result}')