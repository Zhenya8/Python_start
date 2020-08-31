'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл'''

# from googletrans import Translator
#
# file = Translator()
# with open('text_4.txt', 'r+', encoding='utf-8') as f:
#     for line in f:
#         line = file.translate(line, dest="ru")
#         print(line)
#
# # Не успела разобраться с googletrans выводом


rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
result = []

with open('text_4.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split(" - ")
        print(line)
        if line[0] in rus:
            word = rus[line[0]]
            result.append(word + ' - ' + line[1])
    print(result)

with open('text_4.txt', 'w', encoding='utf-8') as f:
    f.writelines(result)


