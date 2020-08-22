""" Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом
английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
текстовый файл. """

from pathlib import Path

numerals = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}

parent_dir = Path(__file__).parent
source_file = parent_dir.joinpath('text_file4_source.txt')
receiver_file = parent_dir.joinpath('text_file4_receiver.txt')

if source_file.exists():
    with source_file.open() as sf, receiver_file.open('w') as rf:
        for line in sf:
            try:
                num = line.split()[0]
                line = line.replace(num, numerals.get(num, num))
                rf.write(line)
            except IndexError:
                continue
else:
    print('Файл источник не существует')
