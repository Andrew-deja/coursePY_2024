# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, sep = ','): # разделитель по умолчанию - ','
    new_str_1 = set(str1.split(sep)) # приводим к типу множество для дальнейшей работы с методом
    new_str_2 = set(str2.split(sep))
    inter_str = new_str_1.intersection(new_str_2)
    return list(inter_str) # возвращаем список

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group,
                                               participants_second_group,
                                               '|') # передаем собственный разделитель
common_participants.sort() # сортируем список
print(common_participants)
