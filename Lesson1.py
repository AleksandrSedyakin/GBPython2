# 1 часть задания
wts = 'Hello guys'
some_num = 7
print(wts, 'here we are,', some_num, 'bodies')
wts = input('Скажи привет ')
some_num = input('Теперь напиши число: ')
print(wts, 'вот и мы,', some_num, 'дубаломов')

# 2 часть задания
sec = int(input('Напишите время в секундах: '))
min = sec // 60
hours = min//60
print ('Время: {}:{}:{}' .format(hours, (min % 60), sec % 60))

# 3 часть задания
num = int(input('Введите число: '))
print(num + num*2 + num*3)

# 4 часть задания
num2 = input('Введите целое положительное число: ')
simbols = len(num2)
max_num = 0
while simbols > 0:
    if max_num < int(num2[simbols-1]):
       max_num = int(num2[simbols - 1])
    simbols -= 1
print(max_num)

# 5,6 часть задания
pribil = int(input('Какая у вас итоговая выручка за год в рублях? '))
trati = int(input('Сколько вы потратили? '))
if pribil > trati:
    print('Вы крутаны, в плюсе остались, конгарюляции!')
    print('Рентабельность у вас:', pribil/trati)
    chel = int(input('Скок у вас человек в фирме? '))
    print('Каждый ваш сотрудник заработал: ', pribil/chel)
elif pribil == trati:
    print('Можно было и лучше, но тоже не плохо!')
else:
    print('Так можно и без штанов остаться, ребят, старайтесь лучше!')

# 7 часть задания
a = int(input('Привет, сколько ты пробегаешь на настоящий момент, в км? '))
b = int(input('Ок, а сколько бы хотел пробегать в дальнейшем? '))
day = 1

print('Вот тебе план план пробежек, для достижения желаемого результата, если будешь увеличивать дистанцию на 10% ежедневно: ')
while a < b:
    print('{}-й день: {}' .format(day, a))
    a += a*0.1
    day += 1
print('{}-й день: {}' .format(day, a))








