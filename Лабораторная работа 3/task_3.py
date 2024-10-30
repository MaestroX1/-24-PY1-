# TODO  Напишите функцию count_letters
def count_letters(text):
    count_letters_dict = {}
    for i in text.lower():
        if i.isalpha() and i not in count_letters_dict:
            count_letters_dict[i] = 1
        elif i.isalpha() and i in count_letters_dict:
            count_letters_dict[i] += 1
    return count_letters_dict

# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters_dict):
    frequency_dict = {}
    for k, v in letters_dict.items():
        frequency_dict[k] = v / sum(letters_dict.values())
    return frequency_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
for k, v in calculate_frequency(count_letters(main_str)).items():
    print(f'{k}: {format(v, ".2f")}')
