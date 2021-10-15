# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

products, order = [], 1
name, price, amount = None, None, None

while True:
    if name is None:
        cnt = input('Введите наименование товара:')
        if not cnt.isalnum():
            print('Наименование товара должно быть заполнено!')
            continue

        name = cnt

    if price is None:
        cnt = input('Введите цену товара:')
        if not cnt.isdigit():
            print('Цена должна быть числом!')
            continue

        price = float(cnt)

    if amount is None:
        cnt = input('Введите количество:')
        if not cnt.isdigit():
            print('Количество должно быть целым числом!')
            continue

        amount = int(cnt)

    cnt = input('Введите единицы измерения:')
    if not cnt.isalpha():
        print('Единица изменерения должна быть заполнена!')
        continue

    unit = cnt

    products.append((
        order,
        {
            'name': name,
            'price': price,
            'amount': amount,
            'unit': unit
        }
    ))

    name, price, amount = None, None, None
    order += 1

    print(products)

    a = input('Завершить ввод информации? (y/N)) ')
    if a.lower() == 'y':
        break

results = {
    'name': [],
    'price': [],
    'amount': [],
    'unit': set()
}

for _, item in products:
    results['name'].append(item['name'])
    results['price'].append(item['price'])
    results['amount'].append(item['amount'])
    results['unit'].add(item['unit'])

print(results)
