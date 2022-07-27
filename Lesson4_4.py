my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

my_list_repeat_index = [el_index for el_index in range(len(my_list) - 1) if my_list.count(my_list[el_index]) > 1]

for elem in my_list_repeat_index:
    my_list.remove(my_list2[elem])

print(my_list)


