# Функция обработки строки
def make_capit (str_list):
    position_of_word = 0
    for word in str_list:
# Проверка на латиницу
        for i in range(len(word)):
            if word[i] >= 'a' and word[i] <= 'z':
                None
            else:
                print('ЛАТИНСКИМИ, маленькими! Е, мае!')
                return ['Кусок', 'Имбецила']
        word = word.capitalize()
        str_list[position_of_word] = word
        position_of_word += 1
    return str_list

# Ввод слов, вызов функции
slova = input('Введите слова через пробел маленькими латинскими буквами: ')
slova = make_capit(slova.split())
for word in slova:
    print(word, end=' ')