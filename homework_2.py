# 1 Задача
# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
#     x = int(input())
#     if x == 0:
#         count_zero += 1
#     else:
#         count_one += 1
# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)

# Задача 2
# summa = int(input())
# proiz = int(input())
# res_x = None
# res_y = None
# for x in range(1001):
#     for y in range(1001):
#         if x+y == summa or x*y == proiz:
#             res_x = x
#             res_y = y
#     if res_x is not None:
#         print(res_x, res_y)
#     break
# Задача № 3
# n = int(input())
# m = 1
# while m < n:
#     if(m < n):
#         if (m * 2 > n):
#             break
#         else:
#             m = m * 2
#             print(m)
# family = 'Targaryen'
# Dragon = 'pet'

# |||||||||||||||||||||||||||||||| LESSON 2


# list_1 = [1, 2, 3, 5]
# print(*list_1) # 1, 2, 3, 5
# print(len(list_1)) #4
# # for i in list_1:
# #     print(i)
# # print(len(list_1))
# # print(list_1[3]) # 5
# # print(list_1[-2]) # 3

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8)
# print(list_1) #[1, 5, 8]

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1) # [[0][0, 1][0, 1, 2][0, 1, 2, 3][0, 1, 2, 3, 4]

# Удаление последнего элемента списка
# list_1 = [12, 7, -1, 21, 0]
# a = list_1.pop()
# print(a)
# print(list_1.pop()) # 0
# print(list_1) #[12, 7, -1, 21]
# print(list_1.pop()) #21
# print(list_1) #[12, 7, -1]
# print(list_1.pop()) #-1
# print(list_1) #[12,7]

# # Удаление конкретного элемента из списка
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) #[7, -1, 21, 0]
#
# # Добавление элемента на нужную позицию
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11)) # 2 - позиция куда вставить, 11 вставляемое числор
# # print(list_1) #[12, 7, 11, -1, 21, 0]


# СРЕЗЫ
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) #1
# print(list_1[1]) #2
# print(list_1[len(list_1)-1])  # (list_1[-1])# 10
# print(list_1[-5])# 6
# print(list_1[:]) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2])#[1,2] начало:конец
# print(list_1[len(list_1)-2:]) # 9,10
# print(list_1[len(list_1):2]) # 9,10
# print(list_1[2:9]) #[3,4,5,6,7,8,9]
# print(list_1[0:len(list_1):6]) # [1,7]
# print(list_1[::6]) # [1,7]


# КОРТЕЖИ = это неизменяемый СПИСок
#АНИМАЕТ МАЛО памяти и нельзя изменить в программе (пароли тп)

# t = ()
# print(type(t))
# t = (1)
# print(type(1)) #<class 'tuple'> #<class 'int'>
# t = (1, 5, 3,)
# print(type(t))
#
# v = [1, 8, 9]
# print(v)
# print(type(v))
#
# v = tuple(v)
# print(v)
# print(type(v))
# # a, b = 1, 2
# a,b,c = v
# print(a,b,c)

#Отличик от списка
#t = (1,2,3,5,)
#print()
# for i in range(len(t)):
    # print(t[i])
#t[0] = 2 # Ошибка


# СЛОВАРИ!!!!!!!!!
# Это неупорядоченные коллекции произвольных объектов с доступом по ключу.
# В списках в качестве ключа используется индекс элемента.
# В словаре для определения элемента используется значение ключа (строка, число)
# d = {}
# d = dict() # Также является словарем, аналогия выше
# d["q"] = 'qwerty' # В нашем словаре есть ключ q по которму мы обратимся и будет qwerty
# print(d)
#
# d["w"] = 'werty'
# print(d['q']) # qwerty

# dictionary = {}
# dictionary = {"up": "↑", "left": "←", 'down': "↓", "right": "→"}
# print(dictionary) # ["up": "↑", "left": "←", 'down': "↓", "right": "→"]
# print(dictionary['left'])
# del dictionary['left'] # Удаление элемента
# for item in dictionary:
    # print('{}: {}'.format(item, dictionary[item]))
    # print(item)
# print (dictionary.items())
# for (k,v) in dictionary.items():
#     print(k,v) # k - КЛЮЧ, V - значение!!!!!!!!!!!!!!!!!!!!!!


# dictionary[895] = 98998
# print(dictionary)



# МНОЖЕСТВА!!!!!!!!!!!!
# Множества содержат в себе уникальные элементы, не обязательно
# oдно множество может содержать значения любы[ типов. Если у вас два множества, вы можете совершать
# над ними любые стандартные операции, например объединение, пересечение и разность.

# colors = {'red', 'green', 'blue'}
# print(colors) # 'red', 'green', 'blue'
# colors.add('add')
# # colors.remove('red')
# colors.discard('red')
# print(colors)
#colors.clear() # Удаляет все
#print(colors)
#q = set() # Удаляет


#ОПЕРАЦИИ СО МНОЖЕСТВАМИ!!!

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13}
# i = a.intersection(b) # A пересечение Б i = {8, 2, 5}
# d1 = a.difference(b) # Из А убрать Б {1,3} Из А убирать все значения которые сть в Б
# dr = b.difference(a) # dr = {13,21}
# q = a.union(b).difference(a.intersection(b)) # ! ПЕРВОВЫЕ ВЫРАЖЕНИЕ В СКОБКАХ, 1. Найти пересечение А и Б, объяденеиям и находим разность между а И Б

# a = {1, 8, 6}

# b = frozenset(a) # Замородить А не сможет его изменять

#LIST Compehension
#list_1 = [exp for item in iterable] #
# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1)

# list_1 = [i for in range (1, 101)] # Мы добавляем в наш список i, где i - for i in range
#   Добавление четный числе
# list_1 = [i for i in range(1, 101) if i % 2 == 0]
# Допустим мы хотим создать пары каждому из чисел (кортежи)
# list_1 = [(i,i) for i in range(1, 101) if i % 2 == 0] #([2,2], (4,4))
# Также можно умножать, делить, прибавлять, вычитать. Например, уммножить значение на 2
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) #[0,4,8,12,16