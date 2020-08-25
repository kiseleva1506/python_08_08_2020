""" Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке. """

from pathlib import Path

file_name = Path(__file__).parent.joinpath('text_file2.txt')

if file_name.exists():
    with file_name.open() as f:
        lines = f.readlines()
        word_count = [(ind, len(line.split())) for ind, line in enumerate(lines, 1)]

        print(f'Строк в файле: {len(lines)}')
        for i, el in word_count:
            print(f'{i}: {el}')
else:
    print('Файл не существует')
