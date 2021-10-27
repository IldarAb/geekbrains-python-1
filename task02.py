# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.

try:
    with open('text_file1.txt', 'r') as my_file:
        content = my_file.read()
        print(f'Содержимое файла: \n{content}')
        with open('text_file1.txt', 'r') as my_file:
            content = my_file.readlines()
            print(f'Количество строк в файле: {len(content)}')
            for i in range(len(content)):
                print(f'Количество слов в {i + 1} - ой строке {len(content[i].split())}')
except IOError:
    print("Файл не обнаружен")