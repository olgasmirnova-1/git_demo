# s = 'hello world'

# print(s.replace('l', '!', 1))
# print(s.replace(' ', ''))
#
# print(s.count('l'))
w = 'Денисов Денис Денисович'
w1 = '1, 2, 3, 4, 5'
# print(w.split()) #список
# print(w.split('е')) #делит список
# print(w1.split(',', maxsplit=2))
# w2 = w1.split(',')
# print(type(''.join(w1)))
# print(''.join(w1))
# w3 = '       123hello123 '
# print(w3.strip().strip('123')) #убирает символы

# w4 = 'hello world'
# print(w4.find('e'))
# print(w4.find('o', 2, 5))
# print(w4.index('e', 2, 5)) find without error, index with error


# w5 = 'naMe world title'
# print(w5.upper())
# print(w5.lower())
# print(w5.title())
# print(w5.capitalize())
# print(w5.swapcase())

w6 = '1234'
w7 = 'Qwerty'
w8 = '123a'
# print(w6.islower())
# print(w7.islower())
# print(w8.islower())
# print(w6.isupper())
# print(w7.isupper())
# print(w8.isupper())
# print(w6.isdigit())
# print(w7.isdigit())
# print(w8.isdigit())

# print(w6.isalpha())
# print(w7.isalpha())
# print(w8.isalpha())

# a = int(input('Введите цифру: '))
#
# if a % 2 == 0:
#     if a % 10 == 0:
#         print(f"{a} делится на 2 и на 10")
#     else:
#         print(f"{a}':  делится на 2, но не делится на 10")
# else:
#     print(f"{a} не делится на 2")
#
# q = int(input('Введите вашу отметку: '))
# if q >= 90:
#     print(5)
# elif q >= 80:
#     print(4)
# elif q >= 70:
#     print(3)
# else:
#     print(2)

# if 10 < 20:
#     pass
# print(6)

# number = int(input('your number: '))
# if number < 10:
#     print('One sil')
# elif 10 <= number <= 99:
#     print('Two')
# elif 100 <= number <= 999:
#     print('Three')
# else:
#     print('dont know')

# x, y = 55, 55
# s = x if x > y else y
# print(s)
# if x > y:
#     print(x)
# else:
#     print(y)
# print(s)

# value = 5
# match value:
#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case 3:
#         print(3)
#     case 4:
#         print(4)
#     case 5:
#         print(5)
#     case _:
#         print('такой цифры нет')

# c = 0
# while c < 5:
#     print('Hello')
#     c += 1
#
# c = 0
# while c < 5:
#     if c % 2 == 0:
#         print('Hello')
#     else:
#         print(8)
#     c += 1
# text = int(input('Введите число: '))
# count = 0
# while text != 'stop':
#     num = int(text)
#     count += num
#     text = input('Для продолжения введите число, если не хоттите, то введите stop: ')
# print(f"Сумма чисел равно {count}")
#

# num = 10
# for i in range(1, num+1, 2):
#     print(i)

# string_1 = 'Hello'
# for i in range(len(string_1)):
#     print(i)

string_1 = 'HeLl5o'
# for i in range(len(string_1)):
#     print(string_1[i])

# for i in string_1:
#     print(i)

# for i in range(len(string_1)):
#     if string_1[i].islower():
#         print(i, string_1[i])
#
# for i in range(len(string_1)):
#     if string_1[i].isupper():
#         print(i, string_1[i])
#
# for i in range(len(string_1)):
#     if string_1[i].isdigit():
#         print(i, string_1[i])
repeat = int(input())
string = input()
def repeat_str(repeat, string):
    repeat = int(input())
    string = input()
    return repeat * string
    return "".join([string]*repeat)