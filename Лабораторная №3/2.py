# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, delimiter=','):
    set1 = set(str1.split(delimiter))
    set2 = set(str2.split(delimiter))
    participants = sorted(list(set1.intersection(set2)))
    return participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group, participants_second_group, delimiter=',')
# TODO Провеьте работу функции с разделителем отличным от запятой
print(result)