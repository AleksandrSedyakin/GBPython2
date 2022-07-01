# # 1
# some_list = [123, 'hallo', True, 24.5]
# for elem in some_list:
#     print(type(elem))

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