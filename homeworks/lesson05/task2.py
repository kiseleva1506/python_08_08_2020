""" Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке. """

from pathlib import Path

file_name = Path(__file__).parent.joinpath('text_file2.txt')

if file_name.exists():
    with file_name.open() as f:
        lines = f.readlines()
        word_count = [len(line.split()) for line in lines]
        print(f'Строк в файле: {len(lines)}')
        for i, el in enumerate(word_count, 1):
            print(f'{i}: {el}')
else:
    print('Файл не существует')
