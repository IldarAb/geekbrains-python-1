# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

result_dict = {
    'Зима': ['1', '2', '12'],
    'Весна': ['3', '4', '5'],
    'Лето': ['6', '7', '8'],
    'Осень': ['9', '10', '11']}

result_list = [
    ['Зима', ['1', '2', '12']],
    ['Весна', ['3', '4', '5']],
    ['Лето', ['6', '7', '8']],
    ['Осень', ['9', '10', '11']]]

while True:
    month_number = input('Пожалуйста введите номер месяца (от 1 до 12): ')
    if month_number not in sum(result_dict.values(), []):
        print('Вы ввели ошибочный номер!')
        continue
    break

for season, months in result_dict.items():
    if month_number in months:
        print(f'С помощью словаря определено, что месяц с номером {month_number} это {season}')

for season, months in result_list:
    if month_number in months:
        print(f'С помощью списка определено, что месяц с номером {month_number} это {season}')
