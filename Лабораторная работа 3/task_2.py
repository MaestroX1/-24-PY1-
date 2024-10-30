# TODO Напишите функцию find_common_participants
def find_common_participants(s1, s2, razd=','):
    s1, s2 = s1.split(razd), s2.split(razd)
    s_vsex = s1 + s2
    s_obsh = []
    for i in s_vsex:
        if (i not in s_obsh) and (s_vsex.count(i)>1):
            s_obsh.append(i)
    s_obsh.sort()
    return s_obsh


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))