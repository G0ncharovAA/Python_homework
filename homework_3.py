from random import sample

# Урок 3. Данные, функции и модули в Python
#
# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
#
# out
# [10, 2, 3, 8, 9]
# 22
#
# Решение:


size = int(input("Введите размер списка:"))
if size < 1:
    raise ValueError("Некорректный размер списка")

items_range = range(-25, 25)  # по умолчанию
seq = sample(items_range, size)
print(f"Исходный список {seq}")
summ = 0

for num in seq[::2]:
    summ += num

print(f"Сумма элементов на нечетных позициях: {summ}")


# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
#
# out
# [2, 5, 8, 10]
# [20, 40]
#
# Решение:

size = int(input("Введите размер списка:"))
if size < 1:
    raise ValueError("Некорректный размер списка")

items_range = range(-50, 50)  # по умолчанию
seq = sample(items_range, size)
print(f"Исходный список {seq}")

output = []

starting_index = 0
center_index = size // 2
ending_index = size - 1

while starting_index < center_index:
    output.append(seq[starting_index] + seq[ending_index])
    starting_index += 1
    ending_index -= 1

if size % 2 != 0:
    output.append(seq[center_index])

print(f"Список сумм пар элементов: {output}")


# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
#
# in
# 88
# out
# 1011000
#
# Решение:


num = int(input("Введите десятичное число:"))

output = []

while num > 0:
    output.insert(0, num % 2)
    num //= 2

binary = "".join(map(str, output))
print(f"Двоичная запись числа: {binary}")


# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
#
# Решение:

def divide_by_hundred(num):
    return num / 100

def extract_fractional_part(float_num):
    return float_num % 1

size = int(input("Введите размер списка:"))
if size < 1:
    raise ValueError("Некорректный размер списка")

items_range = range(0, 1000)  # по умолчанию
seq = list(map(divide_by_hundred, sample(items_range, size)))
print(f"Исходный список {seq}")

seq_fractional = list(map(extract_fractional_part, seq))
print(f"Cписок дробных частей {seq_fractional}")

minimum = min(seq_fractional)
maximum = max(seq_fractional)
print(f"Минимальное {minimum}, и максимальное {maximum} значение дробной части; разница = {maximum - minimum}")

# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
#
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
#
# Решение:

# Сперва хотела по-простому, через prev и pre_prev,
# но очень быстро поняла что нужно по-правильному: рекурсивно да с мемоизацией
def fib(n, memo=dict()):
    if n == 0:
        memo[n] = 0
        return 0
    elif n == 1:
        memo[1] = 1
        return 1
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = fib(n-1, memo) + fib(n-2, memo)
            return memo[n]


n = int(input("Введите число:"))

if n < 1:
    raise ValueError("Некорректное число элементов")

seq = [0]

for i in range(1, n+1):
    curr = fib(i)
    seq.append(curr)
    seq.insert(0, curr * ((-1) ** (i+1)))

print(f"Негафибоначчи: {seq}")
