# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями
# обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
# элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

result_list = []

while True:
    item = input('Введите значение элемента списка:')
    result_list.append(item)

    a = input('Продолжить ввод значений элементов списка? (y/n):')
    if a.lower() == 'n':
        break

last_idx = len(result_list) - 1

for idx, _ in enumerate(result_list):
    if idx % 2 == 0 and idx < last_idx:
        result_list[idx + 1], result_list[idx] = result_list[idx:idx + 2]

print(result_list)
