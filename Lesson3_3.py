# Определяем функцию
def my_func(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return
    make_list = [a, b, c]
    make_list.sort()
    return make_list[1] + make_list[2]

# Получение чисел от пользователя
num_list = []
for i in range(0, 3):
    num_list.append(input('Введите число: '))

# Функция пошла
print(my_func(num_list[0], num_list[1], num_list[2]))

