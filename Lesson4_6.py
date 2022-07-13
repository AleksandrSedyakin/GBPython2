from itertools import count, cycle

# итератор чисел с - по
def my_num_gen (start, end):
    for i in count(start):
        if i > end:
            break
        yield i

# итератор списка, rounds - количество итераций
def my_list_cycle (list, rounds):
    for i in cycle(list):
        if rounds <= 0:
            break
        rounds -= 1
        yield i

# вызов итератора чисел
for y in my_num_gen(3, 20):
    print(y)

my_list = [12345, 'hey_guys', 'вышли погулять опять']

# вызов итератора списка
for u in my_list_cycle(my_list, 2):
    print(u)

