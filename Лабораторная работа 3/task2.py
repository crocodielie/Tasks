# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2, sep=","):
    new_list = []
    str1 = str1.split(sep)
    str2 = str2.split(sep)
    for i in str1:
        for j in str2:
            if i == j:
                new_list.append(i)
    return new_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
separator = "|"

# TODO Провеьте работу функции с разделителем отличным от запятой

common_participants = find_common_participants(participants_first_group, participants_second_group, '|')
print(common_participants)
