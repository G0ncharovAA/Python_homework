from random import sample
from itertools import groupby

# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
#
# in
# 9
#
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
#
# in
# 10
#
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]
#
# Решение:

size = int(input("Введите размер последовательности: "))
if size < 1:
    raise ValueError("Некорректный размер последовательности")

items_range = range(100)  # по умолчанию
source_list = sample(items_range, size)
print(f"Исходная последовательность {source_list}")

shifted_list = source_list[1::]
print(f"Сдвинутая последовательность {shifted_list}")

truncated_list = source_list[:len(source_list) - 1:]
print(f"Обрезанная последовательность {truncated_list}")

zipped_list = list(zip(truncated_list, shifted_list))
print(f"Совмещённая последовательность {zipped_list}")

filtered_list = list(filter(lambda num: num[0] < num[1], zipped_list))
print(f"Отфильтрованная последовательность {filtered_list}")

output_list = list(map(lambda num: num[1], filtered_list))
print(f"Результирующая последовательность {output_list}")


# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
#
# in
# 100
#
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]
#
# in
# 424
#
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189,
# 200, 210, 220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 378,
# 380, 399, 400, 420]
#
# Решение:


n = int(input("Введите значение N: "))
if n < 20:
    raise ValueError("Некорректное значение N")

items_range = range(20, n + 1)
source_list = list(items_range)
print(f"Исходная последовательность {source_list}")

filtered_list = list(filter(lambda x: x % 20 == 0 or x % 21 == 0, source_list))
print(f"Отфильтрованная последовательность {filtered_list}")

# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
#
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
#
# out
#
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}
#
# Решение:

names = []
with open('russian_names.txt', encoding="utf-8") as input_file:
    names.extend(input_file.read().split("\n"))

print(f"Плоский список имён: {names}")

# Ну почему Python не может вернуть map<key, list<value>> как все нормальные языки? Одни слёзы
names_by_letter_raw = groupby(names, key=lambda name: name.lower()[0])

names_by_letter = dict()
for key, value in names_by_letter_raw:
    names_by_letter[key] = list(value)

print(f"Сгруппированный список имён: {names_by_letter}")

search_letter = input("Введите букву для поиска: ")
print(f"Имена, начинающиеся с буквы {search_letter}: {names_by_letter[search_letter]}")
