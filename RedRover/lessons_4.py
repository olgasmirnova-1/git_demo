# def calc(a, b=1):
#     return a - b
#
# print(calc(b=4, a=9))

# def person(age, f_name, l_name):
#     return f'Hello, my name is {f_name} {l_name}. I am {age} years old'
#
# print(person(25, 'Anna', 'Smith'))

# print(sum([5, 6, 7, 4]))
# print(min([5, 6, 7, 4]))
# print(max([5, 6, 7, 4]))

# def pattern(lenght, chart1, chart2):
#     return(chart1 + chart2) * lenght + chart1
# print(pattern(8, "*", "-"))

# lambda argument: manipulate(argument)
# lambda N: N*N

# mult = lambda x, y: x-y
# print(mult(5, 6))
# l = [20, 'str', 15, 18, 'yes', 'apple', 48, 40.5]
# l1 = [20, 15, 8, 7, 6]

# filtered = list(filter(lambda x: not isinstance(x, int) or isinstance(x, float) and x % 2 != 0, l))
# print(*filtered)
# power = list(map(lambda x: x ** 2 if isinstance(x, int) else x, l))
# print(power)

# from functools import reduce
# result = reduce(lambda x, y: x - y, l1)
# print(result)


# def my_decorator(func):
#     def wrpapper(arg):
#         print('Я - обертка!')
#         func(arg)
#         print('Завернули')
#     return wrpapper
#
# @my_decorator
# def say_hello(name):
#     print(f'Hello, {name}')
# say_hello('Sam')

# say_hello = my_decorator(say_hello)
# say_hello()

# def milk(func):
#     def wrapper():
#        print('hot milk')
#        func()
#     return wrapper
# def sugar(func):
#     def wrapper():
#        print('sugar')
#        func()
#     return wrapper
# @sugar
# @milk
# def coffee():
#     print('Coffee')
# coffee

# import datetime
# # print(datetime.date.today())
# bdate = 1980
# current_date = datetime.date.today()
# age = current_date.year - bdate
# current_month = current_date.month
# print(age)
# print(current_month)

# import math as m
# l1 = [1, 20, 30, 55]
# print(m.prod(l1))
# import module
# print(module.hello('Sam'))
# from module import hello, sum
# from module import *
#
# print(hello('Sonya'))
# print(sum(5, 88))

# print(dir(__builtins__))

# print(dir(__builtins__.__dict__))
# print(globals())
# print(f'locals: {locals()}')
# var = 'global'
# def func1():
#     def local():
#         print(var)
#     local()
# func1()
#
# var = 'global'
# def func1():
#     var = 'enclosed'
#     def local():
#         var = 'local'
#         print(var)
#     local()
# func1()
# print(f'Outside {var}')
#
# import time
# print(time.perf_counter())
# HomeWork
# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
     # периметр квадрата, площадь квадрата и диагональ квадрата.
import math
from math import sqrt

# def square(a):
#     return (a * 4, a**2, round(sqrt(a**2*2), 2))

# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

# def employee(**kwargs):
#     for k, v in kwargs.items():
#         print(f'{k}:{v}')
# employee(name='Jon', l_name = 'Smirnoff', age= 35, position = 'dev')
#
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа

# my_list = [20, -3, 15, 2, -1, -21]
# l5 = []
# list(filter(lambda x: l5.append(x) if x > 0 else x, my_list))
# print(l5)

# filtered = list(filter(lambda x: not isinstance(x, int) or isinstance(x, float) and x % 2 != 0, l))
# power = list(map(lambda x: x ** 2 if isinstance(x, int) else x, l))
# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
from functools import reduce

# my_list = [20, -3, 15, 2, -1, -21]
# result = reduce(lambda x, y: x*y, my_list)
# print(result)
# pl = reduce(lambda x, y: x*y, [x for x in my_list if x > 0])
# print(pl)
# result = reduce(lambda x, y: x - y, l1)
# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
# import time
# def my_dec(func):
#     def wrapper():
#         start_time = time.perf_counter()
#         # print(start_time)
#         func()
#         end_time = time.perf_counter()
#         timeall = end_time - start_time
#         print(timeall)
#         print(f'This is time ex for function {timeall}')
#     return wrapper
# @my_dec
# def test_1():
#     a = 5 * 8
#     # print(a)
# test_1()

# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
from my_calc import *

def test():
    print(hello('Soffie'))
    print(sum(5, 9))
    print(min(7, 1, 3))
    print(goodBye('Soffie'))
    print(time())
