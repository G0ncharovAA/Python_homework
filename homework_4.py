from decimal import *
from random import sample

# Урок 4. Данные, функции и модули в Python. Продолжение
# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
#
# out
# 9.000000
#
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
#
# out
# 8.988
#
# Решение:


getcontext().clear_flags()
d = int(input("Введите желаемую точность: "))
getcontext().prec = d
r = Decimal(input("Введите вещественное число: "))

print(f"Число {r:.{d}} с точностью {d} знаков")


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
#
# in
# 54
#
# out
# [2, 3, 3, 3]
#
# in
# 9990
#
# out
# [2, 3, 3, 3, 5, 37]
#
# in
# 650
#
# out
# [2, 5, 5, 13]
#
# Решение:

n = int(input("Введите натуральное число N: "))

prime_dividers = []
for i in range(n - 1, 1, -1):
    is_prime = 0
    if (n % i == 0):
        for j in range(i - 1, 1, -1):
            if (i % j == 0):
                is_prime = is_prime + 1
        if (is_prime == 0):
            prime_dividers.append(i)


print(f"Простые множители числа: {prime_dividers}")

# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
#
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
#
# in
# -1
#
# out
# Negative value of the number of numbers!
# []
#
# in
# 10
#
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]
#
# Решение:

size = int(input("Введите размер последовательности:"))
if size < 1:
    raise ValueError("Некорректный размер последовательности")

items_range = range(100)  # по умолчанию
seq = sample(items_range, size)
seq.extend(sample(items_range, size))
print(f"Исходная последовательность {seq}")

temp = {}
for i in seq:
    if i in temp:
        temp[i] = False
    else:
        temp[i] = True

output= [i for i in temp if temp[i]]

print(f"Cписок неповторяющихся элементов исходной последовательности {output}")

# 4.* Задана натуральная степень k. Сформировать случайным образом
#  список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
#
# in
# 0
# -1
# 4
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0


def generate_coeffs(k):
    if k < 1:
        raise ValueError("Некорректная натуральная степень")
    items_range = range(-10, 10)  # по умолчанию
    return sample(items_range, k)


def map_coeff_to_string(coeff, k):
    output = ""
    if coeff == 0:
        return output
    elif coeff < 0:
        output += f"-{abs(coeff)}"
    elif coeff > 0:
        output += f"+{abs(coeff)}"

    if k > 0:
        output += f"*x^{k} "
    else:
        output += " "
    return output


def generate_equasion(k):
    coeffs = generate_coeffs(k)
    equasion = ""
    for i in range(k-1, -1, -1):
        equasion += map_coeff_to_string(coeffs[i], i)
    return equasion + "= 0"


def get_equasions(n):
    equasions = []
    for i in range(n):
        k = int(input("Введите натуральную степень k: "))
        equasion = generate_equasion(k)
        print(f"Уравнение: {equasion}")
        equasions.append(equasion)
    return equasions


n = int(input("Введите количество уравнений для генерации: "))
with open("equasions.txt", "w", encoding="utf-8") as output:
    output.write("\n".join(get_equasions(n)))

# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
#
# in
# "poly.txt"
# "poly_2.txt"
#
# out
# The contents of the files do not match!
#
# Решение:


def remove_suffix(equasion):
    return equasion.removesuffix(" = 0")


def add_suffix(equasion):
    return equasion + " = 0"


def split_equasion(equasion):
    return equasion.split(" ")


def join_equasion(equasion):
    return " ".join(equasion)


def prepare_equasion(equasion):
    return split_equasion(remove_suffix(equasion))


def restore_equasion(equasion):
    return add_suffix(join_equasion(equasion))


def summ_equasions(eq1, eq2):
    output = eq1
    output.extend(eq2)
    return output


def prepare_file(num):
    n = int(input("Введите количество уравнений для генерации: "))
    if n < 1:
        raise ValueError("Некорректное количество уравнений")

    with open(f"poly{num}.txt", "w", encoding="utf-8") as output:
        output.write("\n".join(get_equasions(n)))


prepare_file(1)
prepare_file(2)

equasions1 = []
with open('poly1.txt', encoding="utf-8") as input_file:
    equasions1 = input_file.read().split("\n")

equasions2 = []
with open('poly2.txt', encoding="utf-8") as input_file:
    equasions2 = input_file.read().split("\n")

if len(equasions1) != len(equasions2):
    raise ValueError("Неравное количество уравнений в двух файлах")

result_equasions = []
size = len(equasions1)
for i in range(size):
    result_equasions.append(restore_equasion(summ_equasions(
        prepare_equasion(equasions1[i]), prepare_equasion(equasions2[i]))))

summ_content = "\n".join(result_equasions)
print(f"Суммы уранений: {summ_content}")
with open(f"summ.txt", "w", encoding="utf-8") as output:
    output.write(summ_content)


# Никогда!! Никогда больше я не буду писать ничего сложного на Python!
# Динамическая типизация исключает возможность отследить, что именно я передаю и получаю; а изменяемость по
# умолчанию (list1.extend(list2)) приводит к непредскауемым результатам! 
# Не удивительно, что нормальные языки практикуют явную статическую типизацию, или хотя-бы пытаются в неё, как TypeScript.
# И ведь Python тоже поддерживает статическую типизацию, именно с которой следовало бы начать знакомство с ним.
# Неизменяемость по умолчанию(summ_list = list1.extend(list2)) - сравнительно новая фича, но она жизненно необходима
# для реализации более-менее сложных алгоритмов, тем более если речь идёт еще и о параллельных вычислениях.
# 
# Как всегда, благие немерения разработчиков Python сделать проще, удобнее - привели к результату катастрофическому!
# Как всегда, в конкурентной борьбе технологий остаются и побеждают лишь самые мерзкие, 
# вроде двигателей внутреннего сгорания и языков с динамической типизацией.  