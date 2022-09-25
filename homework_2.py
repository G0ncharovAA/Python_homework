from random import randrange

# Урок 2. Знакомство с Python. Продолжение
#
# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27
#
# Решение:

str_num = input('Введите вещественное число: ')
# Не вычитаю единицу для плавающей точки, т.к. её, точки, может и не быть
n = len(str_num)
num = abs(int(float(str_num) * 10 ** n))
digits_sum = 0

while num >= 10:
    digits_sum += num % 10
    num //= 10

digits_sum += num
print(f"Сумма цифр в числе: {'{:.0f}'.format(digits_sum)}")

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]
#
# Решение:

def fact(n, seq):
    if n == 1:
        seq.append(1)
        return n
    else:
        next_value = n * fact(n - 1, seq)
        seq.append(next_value)
        return next_value


n = int(input('Введите число N: '))

if n > 0:
    seq = []
    ending_value = fact(n, seq)
    print(f"Набор произведений чисел от 1 до N:  {seq}")
else:
    print('Пустое множество')


# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
#
#     Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
#
# Решение:

# Совпадает со значением из примера только если округлять
def calc(n):
    return round((1 + (1 / n)) ** n)


n = int(input('Введите число N: '))
seq = []

# range - включает первое значение, но не включает последнее
for i in range(1, n + 1):
    seq.append(calc(i))

if seq:

    print(f"Сумма значений последовательности {seq} равна {sum(seq)}")
else:
    print('Сумма значений пустого множества равна нолю')

# 4. Напишите программу, которая принимает на вход 2 числа.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
#
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15
#
# Решение:

position_one = int(input('Введите первое число: '))
position_two = int(input('Введите второе число: '))
n = abs(int(input('Введите число N: ')))

starting_position = 1
ending_position = n * 2 + 1
positions_range = range(starting_position, ending_position + 1)

if position_one not in positions_range or position_two not in positions_range:
    print('Некорректные позиции')
else:
    seq = []
    for i in range(-n, n + 1):
        seq.append(i)
    print(f"Произведение элементов множества {seq}")
    print(
        f"Находящихся на позициях {position_one} и {position_two} равна {seq[position_one - 1] * seq[position_two - 1]}")


# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
#
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
#
# Решение:

def swap(seq, index1, index2):
    temp = seq[index1]
    seq[index1] = seq[index2]
    seq[index2] = temp


def my_shuffle(seq):
    for i in range(0, len(seq)):
        swap(seq, i, randrange(len(seq) - 1))
