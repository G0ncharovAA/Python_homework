from random import sample
from itertools import groupby, starmap
from os import path

# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.
#
# in
# Number of words: 10
#
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
#
# in
# Number of words: 6
#
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
#
# in
# Number of words: -1
#
# out
# The data is incorrect
#
# Решение:

CHARS_POOL = "абв"


def generate_word(length):
    return "".join(sample(CHARS_POOL, length))  # Нет бы просто list.join()


def generate_words_list(n, length):
    return [generate_word(length) for _ in range(n)]  # Python не умеет нормально генерировать списки


def filter_word(words, word_to_filter):
    return list(filter(lambda word: word != word_to_filter, words))  # Правильно писать list.filter()


words = generate_words_list(int(input("Введите размер списка слов: ")), 3)
print(f"слова: {words}")
words = filter_word(words, "абв")  # значение words здесь изменяется
print(f"слова без абв: {words}")


# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#
# Алгоритм RLE
#
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
#
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
#
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
#
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q
#
# Решение:

def compress_to_rle(source_file_name="source.txt", compressed_file_name="compressed.txt"):
    if path.exists(source_file_name) and not path.exists(compressed_file_name):
        with open(source_file_name) as source_file, open(compressed_file_name, "a") as compressed_file:
            for line in source_file:
                compressed_file.write("".join([f"{len(list(multiplier))}{symbol}" for symbol, multiplier in groupby(line)]))
    else:
        raise OSError("Файл не найден")
    return compressed_file_name


def decompress_from_rle(file_name="compressed.txt"):
    if path.exists(file_name):
        with open(file_name) as file:
            temp = ""
            for line in file:
                symbols = []
                for symbol in line.strip():
                    if symbol.isdigit():
                        temp += symbol
                    else:
                        symbols.append([int(temp), symbol])
                        temp = ""
                print("".join(starmap(lambda multiplier, symbol: multiplier * symbol, symbols)))
    else:
        raise OSError("Файл не найден")


input_file_name = input("Введите имя файла для сжатия: ")
compressed_file_name = compress_to_rle(input_file_name)
print(f"Содержимое сжато в файл: {compressed_file_name}/n")
with open(compressed_file_name) as compressed_file:
    print(compressed_file.read())

decompress_from_rle(compressed_file_name)

