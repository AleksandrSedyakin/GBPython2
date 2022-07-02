# 1
some_list = [123, 'hallo', True, 24.5]
for elem in some_list:
    print(type(elem))

# 2
some_list2 = []
while True:
    elem = input('Вводите числа или буквы, для остановки напишите "стоп" ')
    if elem == 'стоп':
        break
    some_list2.append(elem)
print(some_list2)

count = len(some_list2)
if count % 2 != 0:
    count -= 1

while count > 0:
    if count % 2 == 0:
        count -= 1
        continue
    some_list2[count], some_list2[count - 1] = some_list2[count - 1], some_list2[count]
    count -= 1
print(some_list2)

# 3
season = {
    'зима': [1, 2, 12],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11]
}

month = int(input('Введите числом месяц от 1-12: '))
for key in season.keys():
    if season[key].count(month) == 1:
        print(key)

# 4
stroka = input('Напишите ка несколько слов: ')
split_str = stroka.split()
count = 1
for one_word in split_str:
    if len(one_word) >= 10:
        one_word = one_word[0:11]
    print(count, one_word)
    count += 1

# 5
rait = [7, 5, 3, 3, 2]
while True:
    num = input('Введите целое число, напишите "стоп" чтобы закончить: ')
    if num == 'стоп':
        break
    position_of_num = len(rait) - 1
    while position_of_num >= 0:
        if int(num) <= rait[position_of_num]:
            rait.insert(position_of_num + 1, int(num))
            break
        else:
            position_of_num -= 1
            continue
    if position_of_num == -1:
        rait.insert(0, int(num))

    print(rait)

# 6
list_of_goods = []
number_of_good = 1
CONST_PARAM = ['название', 'цена', 'количество', 'единицы']

while True:
    list_of_param = {}
    exit_mode = 0
    for present_param in CONST_PARAM:
        param = input(F"Введите {present_param} {number_of_good} товара (введите 'стоп' для завершения): ")
        if param == 'стоп':
            exit_mode = 1
            break
        list_of_param[present_param] = param
    if exit_mode == 1:
        break
    cortadge = (number_of_good, list_of_param)
    list_of_goods.append(cortadge)
    number_of_good += 1
print(list_of_goods)

analitic_dict = {}
for present_param in CONST_PARAM:
    skoka_tovarov = len(list_of_goods)
    list_of_param = []
    number_of_param = 0

    while skoka_tovarov > 0:
        list_of_param.append(list_of_goods[number_of_param][1][present_param])
        skoka_tovarov -= 1
        number_of_param += 1
        print(list_of_param)

    analitic_dict[present_param] = list_of_param

print(analitic_dict)


