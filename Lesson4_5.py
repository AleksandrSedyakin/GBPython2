from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]

result = reduce(lambda x, y: x*y, my_list)
print(result)