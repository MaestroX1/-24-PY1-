# TODO Напишите функцию find_common_participants
def find_common_participants(s1, s2, razd=','):
    s1, s2 = s1.split(razd), s2.split(razd)
    s_obsh = list(set(s1).intersection(s2))
    s_obsh.sort()
    return s_obsh
# Переделал с использованием intersection()

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
