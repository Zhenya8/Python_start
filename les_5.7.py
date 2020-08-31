'''Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.'''

import json

counter = 0
pure = 0
average = 0
total_dict = {}
average_profit = {}
total_list = []
with open('text_7.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    for line in content:
        name, firm, profit, coast = line.split()
        pure = int(profit) - int(coast)
        if pure > 0:
            average += pure
            counter += 1
            average_profit.update({'average_profit': average / counter})
        total_dict.update({name: pure})
    total_list.append(total_dict)
    total_list.append(average_profit)
    print(total_list)

with open('text_7.1.json', 'w', encoding='utf-8') as f_json:
    json.dump(total_list, f_json, ensure_ascii=False, indent=4)




