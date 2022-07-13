my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list_len = len(my_list)
list_of_list = [my_list[el+1] for el in range(my_list_len-1) if my_list[el+1] > my_list[el]]
print(list_of_list)