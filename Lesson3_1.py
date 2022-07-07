def delenie (a, b):
    if b == 0:
        print ('Делить на ноль не можно!')
    else:
        print(a/b)

nums = input('Введите 2 числа через пробел: ')
delenie(float(nums[0]), float(nums[2]))