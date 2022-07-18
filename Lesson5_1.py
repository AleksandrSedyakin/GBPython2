with open('Lesson5_1_input.txt', 'w') as f:
    while True:
        str = input('Вводите данные ')
        if str == '':
            break
        f.write(f"{str}\n")