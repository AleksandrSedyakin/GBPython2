with open('Lesson5_6_data.txt', 'r', encoding='utf-8') as fr:
    subject_list = {}
    while True:
        line = fr.readline().strip().split()
        if not line:
            break

        total_num_hours = 0
        for el in line:
            if el.find('(') != -1:
                total_num_hours += int(el[0:el.find('(')])

        subject_list[line[0]] = total_num_hours
    print(subject_list)