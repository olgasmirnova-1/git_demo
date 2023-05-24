# def check_even(a):
#     if a % 2 == 0:
#         print('Yes')
#     else:
#         print('No')
#
# for i in range(15):
#     check_even(i)

# def check_even(a):
#     for i in range(a):
#         if i % 2 == 0:
#             print('Yes')
#         else:
#             print('No')
#
# check_even(10)

# def fun():
#     s = 'Hello'
#     print(s)
# fun()

# def fun():
#     s = 'Hi'
#     print(f'First {s}')
# s = 'Hello'
# fun()
# print(f'Secind {s}')

# age = 17
#
# def print_age():
#     print(age)
# print_age()

# def multi():
#     x = 10
#     y = 5
#
#     def sum_fun():
#         c = 20
#         print(x + y + c)
#     sum_fun()
# multi()

# def multi():
#     x = 10
#     def sum_fun():
#         c = 20
#         print(x + y + c)
#     sum_fun()
# y = 5
# multi()

# def multi(a, b):
#     print(a *b)
# multi(2, 5)

# a, *b, c = [1, 'Hello', 3.5, True]
# print(a, b, c)

# def fun(*args):
#     # lst = args
#     name = args[0]
#     last_name = args[2]
#     print(f'Hello, {name} {last_name}!')
#     # print(lst)
# fun('Olga', 25, 'Smirnova', 55)

# def return_dict(**kwargs):
#     print(kwargs)
# return_dict(a=1, b=2, c=3, dfdf=212, khj='hjg')

#  рекурсия - это функция, которая вызывает сама себя

# def fun(x):
#     if x <= 10:
#         print(x)
#         fun(x+1)
#
# fun(1)
# факториал
# def fact(n):
#     if n == 1:
#         return 1
#     return fact(n-1) * n
#
# print(fact(5))

# def fibonachi(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonachi(n - 1) + fibonachi(n - 2)
# print(fibonachi(10))


# def fun(x):
#     return x ** 3
# print(fun(3))
# lambda - анонимная функция
# a = lambda x: x**3
# print(a(3))

# s = lambda x: x*x
# print(s(5))

# a = lambda x: "Chetnoe" if x % 2 == 0 else "Nexhetnoe"
# print(a(8))

# a = [34, 67, 2, 54, 9]
# a.sort()
# print(a)

# a = [34, 37, 2, 54, 9]
# # a.sort(key=lambda x: x % 2 == 0)
# # print(a)
# print(sorted(a, key=lambda x: x % 2 == 0))

# a = ['aa', 'ab', 'abc', 'xxx', 'a']
# print(sorted(a, key=lambda x: x[0]))
#
# a = [(1, 'ff'), (1, 'ccc'), (3, 'qqq')]
# print(sorted(a, key=lambda x: (x, x[1])))

# def fun(num):
#     return num%10
# a = [44440, 101, 43, 98, 34, 845]
# print(sorted(a, key=fun))

# a = [40, 23, 34, 12, 87]
# print(sorted(a, key=lambda x: x%10))

# a = ['kk 23', 'kk 12', 'rrr 8']
# print(sorted(a, key=lambda x: (x.split()[0], -int(x.split()[1]))))
# # if x%10=0 else for x in range(3)))
# print(ord('C'))
# print(ord('c'))

# a = '1 2 3 4 5'
# b = list(map(int, a.split()))
# c = list(map(str, a.split()))
# print(b)
# print(c)

# def fun(x):
#     return x**2
#
# def fun_n(x):
#     return x**3
#
# a = [1, 3, 5, 7, -67, -6]
# a1 = list(map(str, a))
# print(a1)
# a2 = list(map(abs, a))
# print(a2)
#
# a3 = list(map(fun, a))
# print(a3)
#
# a4 = list(map(fun_n, a))
# print(a4)

# def fun(x):
#     return x > 5
#
# a = [12, 5, 7, 3, 2, 0, -5]

# a1 = list(filter(fun, a))
# print(a1)

# a1 = filter(fun, a)
# print(*a1)


