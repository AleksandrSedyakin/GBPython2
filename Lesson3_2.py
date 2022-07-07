# Определение функции
def print_data(name, year, city, mail, tel):
    print(f"Имя - {name}, Год рождения - {year}, Город проживания - {city}, Email - {mail}, Телефон - {tel}")

# Ввод данных юзером
user_data = ['имя', 'год рождения', 'город проживания', 'email', 'телефон']
position_of_data = 0
for dat in user_data:
    user_data[position_of_data] = input(f"Введите {dat}: ")
    position_of_data += 1

# Погнали
print_data(name=user_data[0], year=user_data[1], city=user_data[2], mail=user_data[3], tel=user_data[4])


