# TODO Найдите количество книг, которое можно разместить на дискете
disk_memory = 1.44 * 1024
count_symbol = 100 * 50 *25
symbols_weight_kb = count_symbol * 4 / 1024
print("Количество книг, помещающихся на дискету:", int(disk_memory//symbols_weight_kb))
