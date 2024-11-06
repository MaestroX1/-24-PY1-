# TODO Напишите функцию для поиска индекса товара
def poisk_pervogo_vhojdenia(l, tovar):
    # Переделал с использованием enumerate()
    for pos, elem in enumerate(l):
        if elem == tovar:
            return pos
    else:
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:

    index_item = poisk_pervogo_vhojdenia(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара

    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
