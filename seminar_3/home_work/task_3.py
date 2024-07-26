# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10
# самых частых. Не учитывать знаки препинания и регистр символов. За основу
# возьмите любую статью из википедии или из документации к языку.

import string

#Создадим текст и приведем его к нижнему регистру.
data = ('97 лет назад ядерная катастрофа уничтожила цивилизацию, превратив планету '
        'в радиоактивную пустыню. Немногим удалось уцелеть: двенадцать околоземных '
        'космических станций объединились в орбитальный комплекс «Ковчег». '
        'Предполагалось, что Земля снова станет обитаемой лишь через сто лет, и '
        'четыре поколения людей терпеливо ждали момента, чтобы вернуться. Долгие '
        'годы люди представляли, как снова ступят на Землю, услышат шелест листвы, '
        'вживую увидят диких зверей и вдохнут воздух не из вентиляционных труб. За '
        'это время выжившие образовали практически тоталитарное государство, в '
        'котором ресурсы бесценны, а человеческая жизнь ничего не стоит. Любое '
        'преступление, совершённое на корабле, карается смертной казнью. И лишь '
        'малолетних нарушителей оставляют в живых и содержат в импровизированной '
        'тюрьме до их совершеннолетия. Суровый канцлер не делает поблажек и не '
        'прощает виновных, таким образом, сохраняя ресурсы и порядок на «Ковчеге». '
        'Но не всех устраивает эта система. Неожиданно на Землю собирают экспедицию. '
        'Первопроходцам предстоит выяснить, пригодна ли планета для заселения. На эту '
        'самоубийственную миссию отправляют сотню несовершеннолетних преступников, '
        'которым и без того грозила смерть. Посадка капсулы прошла неудачно. «Ковчег» '
        'потерял связь с заключёнными, несколько человек погибло при посадке, а космолёт '
        'приземлился далеко от базы с припасами. Голубая мечта превратилась в суровую '
        'реальность. У малолетних нарушителей нет ни еды, ни пресной воды, ни оружия, '
        'ни навыков выживания. За сотню лет родная планета превратилась в дикие джунгли,'
        ' где царствуют жуткие мутанты. Но выжившие подростки готовы вновь завоёвывать Землю.').lower()
MAX_LEN = 10

#Удалим знаки препинания.
new_data = data.translate(str.maketrans('','', string.punctuation)).split(' ')
new_dict = {}

#Добавим в словарь ключ(слово): значение(кол-во повторений в тексте).
for i in new_data:
    new_dict.setdefault(i, new_data.count(i))

#Наведем порядок в словаре(отсортируем его по значению).
sorted_dict = {k: v for k, v in sorted(new_dict.items(), key=lambda item: item[1])}
copy_dict = sorted_dict.copy()
len_dict = len(sorted_dict.keys())
count = 0

#Удалим ненужные эл-ты.
for key, value in copy_dict.items():
    if count < (len_dict - MAX_LEN):
        count += 1
        sorted_dict.pop(key)

print(sorted_dict)
