with open('Lesson5_4_data.txt', 'r') as fr:
    num_of_file = 1
    while True:
        line = fr.readline().strip().split()
        if not line:
            break
        if num_of_file == 1:
            line[0] = 'Один'
        elif num_of_file == 2:
            line[0] = 'Два'
        elif num_of_file == 3:
            line[0] = 'Три'
        else:
            line[0] = 'Четыре'

        with open(f"Lesson5_4_add_data{num_of_file}.txt", 'w', encoding='utf-8') as fw:
            fw.write(line[0] + ' ' + '-' + ' ' + line[2])

        num_of_file += 1