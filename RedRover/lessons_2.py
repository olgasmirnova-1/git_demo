# x = 0
#
# if x == 5:
#     print('Five')
# elif x > 5:
#     print('More than five')
# else:
#     print('Less than five')

# age = int(input('Please, enter your age: '))
#
# if age >= 18:
#     print('Welcome')
# else:
#     print('Go home, baby!')
# import sys
#
# num1 = 0
# num2 = 0
# try:
#
#     num1 = int(input('Number 1: '))
#     num2 = int(input('Number 2: '))
# except ValueError:
#     print('Вы ввели не число')
#     sys.exit()
# operator = input('Operator: ')
# if (num2 == 0 and operator == '/') or num1 > 5:
#
#     try:
#         result = num1 / num2
#         print(f'Result = {result}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')
# else:
#     result = num1 * num2
#     print(f'Result = {result}')

# num = 0
# while num < 5:
#     print(num)
#     # num = num + 1
#     num += 1
# message = 'Hello'
# i = 1
# while i < 6:
#     if i == 3:
#         # break
#     print(i, message)
#     i += 1

#
# message = 'Hello'
# i = 1
# while i < 6:
#     i += 1
#     if i == 3:
#         continue  # пропускает итерация
#     print(i, message)

# for i in range(6):
#     print(i)
# for i in range(1, 6, 2):
#     print(i)

# for i in 'Hello':
#     print(i)

# message = ''
# if message:
#     print(message)
# else:
#     print('The string is empty')

# num = 4
# if not num % 2:
#     print('четное')
# else:
#     print('нечетное')

# def num(a):
#     a = 'hello world'
#     return a
#1
# fillings = int(input('Input fillings: '))
# if fillings <= 0:
#     print('False')
# else:
#     print('True')

# number = int(input('Input number: '))
# if number % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')
#
# Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года,
# которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600). Однако, если год делится без остатка
# на 400, он также считается високосным (1200, 2000)
#
# year = int(input())
#
# if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
#     print('YES')
# else:
#     print('No')
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()

# text = input('Input text: ')
# n = int(input('Input number of iteration: '))
#
# print(text*n)

# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}
name = input('Input your name: ')
if not name.isalpha():
    print('Wrong name, please try again!')
else:
    print(f'Welcome {name}')

    flag = True
    while flag:
        try:
            num1 = int(input('Введите число 1: '))
            num2 = int(input('Введите число 2: '))

            operator = input('Введите оператор: ')
            d = 0
            if operator == '+':
                d = num1 + num2
                print(f'{num1} + {num2} = {d}')
            elif operator == '-':
                d = num1 - num2
                print(f'{num1} - {num2} = {d}')
            elif operator == '*':
                d = num1 * num2
                print(f'{num1} * {num2} = {d}')
            elif operator == '/':
                if num2 != 0:
                    d = num1 / num2
                    print(f'{num1} / {num2} = {d}')
                else:
                    print('На ноль делить нельзя!')
            else:
                print('Неизвестный оператор')

        except ValueError:
            print('Вы ввели не число')
        text = input('Желаете продолжить? Для выхода нажмите "N" или "n". Для продолжения нажмите "Enter": ')
        if text == 'n' or text == 'N' or text == 'Т' or text == 'т':
            flag = False
            print(f'Good Bye, {name}!')


