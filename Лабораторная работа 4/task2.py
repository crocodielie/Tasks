# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = list()

    # TODO считать содержимое csv файла
    data_j = list()
    with open(INPUT_FILENAME, 'r') as file:
        data = csv.DictReader(file, delimiter=',')
        num = 0
        for i in data:
            data_j.append(dict())
            for j in i:
                data_j[num][j] = i[j]
            num += 1

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(data_j, file, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
