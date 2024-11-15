# TODO решите задачу
import json


def task() -> float:
    filename = "input.json"  # задаем имя файла переменной, для удобства
    list_of_dictionary = []  # Для начала, создаем пустой список, в котором в дальнейшем
    # будут словари из файла

    with open(filename, 'r') as file:
        list_of_dictionary = json.load(file)  # считываем файл и заполняем список словарями
    list_of_multiplications = [dict_['score'] * dict_['weight'] for dict_ in list_of_dictionary]
    # используем list_comprehension - создаем новый список на основе произведения значений словаря
    # и с помощью функции sum() суммируем значения списка
    sum_total = sum(list_of_multiplications)
    return round(sum_total, 3) # округляем до 3-го знака и выводим


print(task())
