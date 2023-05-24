# my_list = [1, 'hello', 2.0, True, None, 1, 1]
#
# sentence = 'Python is awesome!'
# print(sentence.split(' ', 1))
# print(sentence.split(' ', maxsplit=10))
# #
# # # print(my_list[0])
# # # print(my_list[-1])
# # # print('Before', my_list)
# # # print(id(my_list))
# # # my_list[0] = 23 #change element in list
# # # print('After', my_list)
# # # print(id(my_list))
# #
# # # my_list.append(sentence)
# # # my_list.insert(-2,sentence)
# # # print(my_list)
# # # print(len(my_list))
# # # print(my_list.count(1))
# # print(my_list.index(None))
#
# my_list = [1, 2, 3, 4, 5]
# print(sum(my_list))
# print(min(my_list))
# print(max(my_list))

my_list = [1, 2, 3, 4, 5, [6, 7, 8, 9, 10, [11, 12]]]
# print(my_list[-1][-1][1])
#
# my_list = [1, 2, 3, 4, 5, [6, 7, 8, 9, 10, [11, 12]]]
my_list.reverse()
# print(my_list)
# print(my_list)

# for loop with list
# for loop with list
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print((num**2))
#
# new_l = [i for i in numbers if i % 2 == 0]
# print(new_l)

# typles
# name = 1, 2, 3
# name = (1, 2, 3)
# name = 1,
# name = (1,)
# print(name)
# print(type(name))

my_tuple = ('apple', 'banana', 'cat')
# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)

# my_tuple[0] = 'ananas'
print(my_tuple)
letters = list(my_tuple)
letters[0] = 'ananas'
print(letters)

# my_tuple = (1, True, 'name', None, 'name', 'name', 25)
# print(my_tuple.index('name'))
# print(my_tuple.count('name'))

# #filtering
# my_tuple = (1, 'name', None, 'name', 'name', 25)
# result = tuple([item for item in my_tuple if isinstance(item, int)])
# # result = [item for item in my_tuple if isinstance(item, int)]
# print(result)
# # isinstance проверят тип данных
#
# # #Tuple methods
# print(f"Sum is: {sum(result)}")
# print(f"Max is: {max(result)}")
# # print(f"Min is: {min(result)}")
# print(f"Length of my_tuple is: {len(my_tuple)}")
# print(f"Length of result is: {len(result)}")

# Iterate tuple with for loop - посчитали количество элементов в кортеже
# for (index, item) in enumerate(my_tuple):
#     print(index, item)
#enumerate функция

# i = 0
# while i < len(my_tuple):
#     print(i, my_tuple[i])
#     i += 1

#Nested list in tuple + можно менять элементы вложенного листа в кортеж
# fruits = ('apple', ['ananas', 'mango'], 'melon')
#fruits[1][0] = 'cherry'
# print(fruits)

#swaping variables
# a = 5
# b = 10
# a, b = b, a #меняем переменные местами
# print(f"a = {a}")
# print(f"b = {b}")

# def sum_it(*args):
#     total = 0
#     for num in args:
#         total = total + num
#     return total
# print(sum_it(4, 5, 10, 6, 20))

# def func(*args):
#     l =[]
#     print(len(args))
#     for item in args:
#         l.append(item*item)
#     return
# print(func(2, 5, 8, 10)

#dictionary
my_dict = {
    'name': 'Anna',
    'last_name': 'Pavlova',
    'age': 30,
    1: 1,
    'department': 'IT'
}
# print(my_dict)
# print(id(my_dict))
# print(my_dict['last_name'])
# my_dict['last_name'] = 'Smirnova'
# print(my_dict)
# print(id(my_dict))
# print(type(my_dict))
# print(len(my_dict))
# my_dict['salary'] = 5000
# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items()) #создает кортеж для каждой пары
# print(my_dict.pop('salary')) #удаляет значение и возвращает
# print(my_dict)
# print(my_dict.get('salary', 'Not found'))

# keys = ['name', 'salary', 'department']
# values = ['Sergey', 5000, 'PR']
# employee = dict(zip(keys, values))
# print(employee)
#
# employee1 = dict(name='John', position='developer', salsry=20000, department='IT')
# print(employee1)

# dictionary = {ключ1: значение1, ключ2:значение2, ...}
# ключ в словаре -  строки, целые числа, числа с плавающей точкой
# значение - любого типа

# SETS - множества (уникальные ключи)
# my_set = {'A', 'B', 'C'}
# my_set = set{}
# my_list = [1, 5, 2, 3, 1, 5, 5, 9]
# print(set(my_list))

# set1 = {1, 2, 3, 'one', 'ten', 20}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# set3 = {1, 2, 3}
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
#print(set2.intersection(set1))
# print(set1.difference(set2))
# print(set1.symmetric_difference(set2))
# print(set1)
# print(id(set1))
# print(set1.remove(1))
# print(id(set1))
# print(set1.add(8))
# print(id(set1))
# print(set1)
#
# fs = frozenset({1, 2, 3})
# print(fs)

# Sorting
# .sorted() - возвращает новый отсортированный список
# .sort() - возвращает первоначальный список в отсортированном виде
# nums = [8, 9, 10, 11, 1.2, 1, 3, 2]
# print(sorted(nums))

#Home work
# #1
# my_list = ['a', 'b', [1, 2, 3], 'd']
# list2 = (my_list[2])
# print(*list2, sep='\n')
#
# list1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# num = [item for item in list1 if isinstance(item, int)]
# print(sum(num))
# litter = [item for item in list1 if isinstance(item, str) and 'a' in item]
# print(litter)
# #второй вариант
# # for i in litter:
# #     if 'a' in i:
# #         print(i)
#
# list2 = ['cat', 'dog', 'horse', 'cow']
# print(tuple(list2))

# 4
# family1 = input('Please, input your family members #1: ')
# family2 = input('Please, input your family members #2: ')
#
#
# count1 = len(family1.split(' '))
# count2 = len(family2.split(' '))
#
#
# if count2 > count1:
#     print(family2)
# elif count1 > count2:
#     print(family1)
# else:
#     print('Equal')

#5
# film = {
#     'title': 'Once again',
#     'director': 'S.S',
#     'year': '2020',
#     'budget': 15000,
#     'main actor': 'S.S',
#     'slogan': 'Newer again!'
# }
#
# print(film.keys())
# print(film.values())
# print(film)
#6
# my_dictionary = {
#     'num1': 375,
#     'num2': 567,
#     'num3': -37,
#     'num4': 21
# }
#
# print(sum(my_dictionary.values()))
#7
# my_list = [1, 2, 3, 4, 5, 3, 2, 1]
# print(set(my_list))

#8
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#
#
# print(set1.intersection(set2))
# print(set1.symmetric_difference(set2))
# print(set1.issubset(set2))
# print(set2.issubset(set1))


def sum_it(num1, num2, num3):
    sum = num1 + num3 + num2
    return sum
print(sum_it(1, 2, 3))
