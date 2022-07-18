from random import randrange
with open('Lesson5_5_data.txt', 'w') as fw:
    num_list = []
    num_of_num = 0
    while True:
        num_list.append(randrange(0, 200))
        num_of_num += 1
        if num_of_num == 20:
            break

    for el in num_list:
        fw.write(f"{el} ")

with open('Lesson5_5_data.txt', 'r') as fr:
    line = fr.readline().strip().split()
    sum_of_num = 0
    for el in line:
        sum_of_num += int(el)
    print(sum_of_num)

