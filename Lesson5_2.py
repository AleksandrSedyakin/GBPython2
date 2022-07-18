with open('Lesson5_2_data.txt', 'r') as lr:
    str_count = 0
    while True:
        line = lr.readline()
        if not line:
            break
        str_count += 1
        line = line.strip()
        line_list = line.split()
        print(f"Количество слов в строке номер {str_count}: {len(line_list)}")
    print(f"Всего в файле {str_count} строки")