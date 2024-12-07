def find_common_participants(string_1, string_2, separator=","):
    return sorted(list(set(string_1.split(separator)).intersection(string_2.split(separator))))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, separator='|'))
