# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    # Десереализация файла csv
    with open(INPUT_FILENAME, 'r') as file:
        reader = [row for row in csv.DictReader(file)]
        # создаем список, состоящий из словарей
        # где каждому столбцу соответствует значение, т.е.
        # {column -> value}

    # TODO Сериализовать в файл с отступами равными 4
    # Сереализация файла json
    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(reader, file, indent=4)
        # с помощью метода dump, закидываем наш список
        # в json файл, указав отступ = 4

# Данный в задаче код - считываем json файл
if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

