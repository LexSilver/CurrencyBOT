# #
# # #
# # # import math
# # #
# # # print(math.trunc(math.fmod(math.fabs(-10000000), 55)+0.3))
# # import os
# #
# # start_path = os.getcwd()
# # print(start_path)
# #
# # from math import log2
# # n = 10000
# # first = n ** 2
# # second = n * log2(n)
# # ratio = first / second
# # print(ratio)
#
#
#
# # def par_checker(stringfdgdfgdfgdfg):
# #     stack = []  # инициализируем стек
# #
# #     for s in stringfdgdfgdfgdfg:  # читаем строку посимвольно
# #         if s == "(":  # если открывающая скобка,
# #             stack.append(s)  # добавляем ее в стек
# #         elif s == ")":
# #             # если встретилась закрывающая скобка, то проверяем
# #             # пуст ли стек и является ли верхний элемент - открывающей скобкой
# #             if len(stack) > 0 and stack[-1] == "(":
# #                 stack.pop()  # удаляем из стека
# #             else:  # иначе завершаем функцию с False
# #                 return False
# #     # если стек пустой, то незакрытых скобок не осталось
# #     # значит возвращаем True, иначе - False
# #     return len(stack) == 0
#
#
# LL = LinkedList()
#
# LL.pushright(1)
# LL.pushleft(2)
# LL.pushright(3)
# LL.popright()
# LL.pushleft(4)
# LL.pushright(5)
# LL.popleft()
#
# print(LL)


# n = int(input())
# f = 1
# while n > 1:
#     f = f * n
#     n = n - 1
#
# print(len(str(f)))

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x


print(len(str(array)))