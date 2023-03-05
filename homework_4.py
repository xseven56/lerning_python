
# Задача No25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# my_string = input("введите строку: ")
# my_string = my_string.split(" ")
# my_string = "a a a b c a a d c d d".split(" ")
#
# my_dict = {}
#
# result_string = ''
# for i in my_string:
#     if my_dict.get(i) is None:
#         my_dict[i] = 0
#         result_string += i + " "
#     else:
#         my_dict[i] = my_dict.get(i) + 1
#         result_string += i + "_" + str(my_dict.get(i)) + " "
#
# print(result_string)


# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# n = int(input("введите количество элементов 1 множества: "))
# m = int(input("введите количество элементов 2 множества: "))
#
# my_set_1 = set()
# my_set_2 = set()
#
# for i in range(n):
#     num = int(input(f"Введите {i+1} элемент: "))
#     my_set_1.add(num)
#
# for i in range(m):
#     num = int(input(f"Введите {i+1} элемент: "))
#     my_set_2.add(num)
#
# print(*(my_set_1 & my_set_2))

# my_set_1, my_set_2 = {int(input()) for i in range(int(input()))}, {int(input()) for i in range(int(input()))}
# print(*(my_set_1 & my_set_2))











