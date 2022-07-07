# Делаем глобальный счетчик чисел
wild_sum = 0

# Функция, которая считает сумму, с проверкой на вшивость, если есть вши, то 0
def make_sum(num_list):
    total_result = 0
    for some_num in num_list:
        if some_num.isdigit():
            total_result += float(some_num)
        else:
            return 0
    return total_result

# Получаем данные от юзера, считаем, выводим
while True:
    input_data = input('Вводите числа через пробел, "Enter" посчитать, "Q" выйти: ').upper()
    input_list = input_data.split()
    print(input_list)
    if input_list.count('Q') != 0:
        input_list.pop(input_list.index('Q'))
        wild_sum += make_sum(input_list)
        print(wild_sum)
        break
    else:
        wild_sum += make_sum(input_list)
        print(wild_sum)
