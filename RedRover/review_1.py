# print(1, 2, 3, sep='!', end='?')
# print("""\n*********\n*       *\n*       *\n*********""")

# a = [ 1, 4, 6, 10, 33]
# for i in a:
#     if i % 2 == 0:
#         print(i, end=' ')

# print(2*(5+2))
# print(2*3**2)
# print(6/2*4)
# print(2+3-5)

# print(abs(-7))
# print(min(8, 4, 7))
# print(max(8, 4, 7))

# print(pow(2, 3)) #возведение в степень, а может быть просто **
# print(round(3.5)) #округление до ближайшего целого числа вэтом случае до 4
# print(round(3.445, 2)) #сколько цифр после запятой округляется

#присваевние
# a = 15
# b = 10
# a += b
# print(a) # += означает a = a + b - для сокращения  можно использовать умножения, деление, вычитание, сложение etc.

#вывод данных
# text = 'Hey'
# text2 = "Hey"
# text3 = """Hello world
# 123
# My"""
# print(text3)
#
# text4 = input()
# print(text4)

# name = "Семен"
# lastName = "Семенович"
# # balance = 100
# balance = int(input("Введите баланс: "))
# print(f"Уважаемый {name} {lastName}, ваш баланс слставляет {balance * 10} рублей")

#дублирование строк
# print("Hello"*5)
# как получить длину строки
# text = "12"
# print(len(text))

# вхождение элемента в строку
# text = "Hello world"
# print('a' in text)

#Индексы
# text = "Hello world"
# print(text[0])
# print(text[len(text)-1])
# print(text[-1])
# print(text[0:4]) # срез

def type_validation(variable, _type):
    print(type(variable))
#     if type(variable) == _type:
#         print('true')
#     else:
#         print('false')
#     pass

