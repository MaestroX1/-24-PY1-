# TODO решите задачу
import json
def task() -> float:

    filename = 'input.json'
    proizv_znach = []
    with open(filename) as file:
        data = json.load(file)

    for i in data:
        proizv_znach.append(i['score'] * i['weight'])
    sum_znach = round(sum(proizv_znach), 3)
    return sum_znach


print(task())
