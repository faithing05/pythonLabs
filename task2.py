# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=','):
    set_group1 = set(group1.split(separator))
    set_group2 = set(group2.split(separator))

    intersection_participants = set_group1.intersection(set_group2)

    return sorted(intersection_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Иванов|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
# TODO Проверьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))