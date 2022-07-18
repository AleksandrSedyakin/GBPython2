with open('Lesson5_3_data.txt', 'r', encoding='utf-8') as ls:
    total_salaries = 0
    count_of_workers = 0
    while True:
        line = ls.readline().strip().split()
        if not line:
            break
        count_of_workers += 1
        total_salaries += float(line[1])
        if float(line[1]) < 20000:
            print(f"{line[0]} ваще лошара!")
    print(f"Средняя з/п по больнице: {total_salaries/count_of_workers}, а говорите мало платят!")