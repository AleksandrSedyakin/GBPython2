# Решение через встроенный оператор
def my_func(x, y):
    return x**y

# Решение через цикл while
def my_func2(x, y):
    delitel = 1
    while y+1 <= 0:
        delitel *= x
        y += 1
    return 1/delitel

print (my_func(2, -4))
print (my_func2(2, -4))


