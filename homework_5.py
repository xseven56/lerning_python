
# def power(a, b):
#     if b < 0:
#         return (1/a)*power(a, b+1)
#     if b > 0:
#         return a*power(a, b-1)
#     else:
#         return 1
# a = int(input('Введитче число а: '))
# b = int(input('Введите число b: '))
# print(power(a,b))

#2 ЗАДАЧА
# def sum(a, b):
#     if b == 0:
#         return a
#     else:
#         if b > 0:
#             return sum(a + 1, b - 1)
#         else:
#             return sum(a - 1, b + 1)
#
# a = int(input('Введитче число а: '))
# b = int(input('Введите число b: '))
# print(sum(a,b))