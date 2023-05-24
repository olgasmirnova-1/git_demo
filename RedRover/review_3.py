# lst = [1, 2, 3, 7, 'poni']
# add
# lst.append('apple')
# print(lst)
#
# lst1 = [55, 77]
# lst.extend(lst1)
# print(lst)
# print(lst + lst1)
# delete
lst = [1, 2, 3, 7, 'poni']
lst1 = [55, 77]
# del lst[0]
# print(lst)
# lst.clear()
print(lst)
# print(lst.index(7))
# lst.remove(7)
# a = lst.pop()
lst.reverse()
print(lst)
# lst.reverse()
# print(a)
# lst2 = lst.copy()
# print(lst)
# print(id(lst))
# print(lst2)
# print(id(lst2))

lst = [1, 2, 3, [45, 55], 4]
print(*lst)
for i in lst:
    print(i)

# [выражение for i in range(10)
# number = [i for i in range(10)]
# number = [i for i in range(10) if i % 2 != 0]
# print(number)

#кортеж - хранение разнотипные значения, неизменяемые
# number1 = [1, 2, 3]
# number2 = (1, 2, 3)
# number1[1] = 20
# # number2[1] = 20
# print(number1)
# # print(number2)

# number = (1, 2, 3, 4)
# number1 = (1,)
# print(type(number1))
# lst = [1, 2, 3, 4, 5, 6]
# tpl = (1, 2, 3, 4, 5, 6)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 2, 3)
# b = list(a)
# b[1] = 15
# c = tuple(b)
# print(type(a))
# print(type(b))
# print(type(c))
# print(c)

# number = (2, 6, 9, 1)
# number1 = sorted(number)
# print(number)
# print(number1)

#множество
# number = {1, 1, 3, 4, 5, 6}
# number1 = {1, 2, 2, 9, 10}
# number2 = {1, 2, 9, 10}
# number3 = {1, 2, 99}
# number.remove(9)
# number.discard(9)
# number.add(88)
# number.update(number3)
# print(number)
# print(number3 in number)
# print(number2 in number3)

# print(number == number1)
# print(number1 == number2)
# number = set()
# print(number)
# # print(type(number))
# print(len(number))
# print(min(number))
# print(sum(number))
# sorted_number = sorted(number)
# print(sorted_number)#и возвращает списко
# number = {1, 1, 3, 2, 4, 5, 6}
# number1 = {1, 2, 2, 9, 10}
# number2 = {1, 2, 9, 10}
# number1 = {188, 238}
# print(number.isdisjoint(number1)) #проверяет есть ли пересечения - нет True

# num = {int(i) for i in input()}
# print(num)

# num = {int(i) for i in range(10)}
# print(num)

#dict
# dct = {
#     'USA': '+100',
#     'Russia': 0,
#     'Turkey': 8
# }

# dct = {}
# dct1 = dict(lake='naroch', river='Sozh', capital='Minsk')
# # dct = dict([['lake', 'naroch'], ['river', 'Sozh'], ['capital', 'Minsk']])
# dct2 = dct | dct1
# print(dct2)
# print(dct)
# print(type(dct))
# print(len(dct))
# if 'France' in dct:
#     print('YES')
# else:
#     print('NO')

# dct = {
#     'USA': '+100',
#     'Russia': 0,
#     'Turkey': 8
# }
# # print(dct.get('USA5', 'Нет такой страны'))
# print(dct.setdefault('France', 88))
# print(dct)
# print(dct.pop('Turkey'))
# print(dct)
# print(dct.popitem())
# print(dct)
# print(*dct, sep='\n')
# for key in dct.keys():
#     print(key)

# for value in dct.values():
#     print(value)

# for key in dct:
#     print(dct[key])

# for key, value in dct.items():
#     print(key, value)

# dct = {
#     'USA': '+100',
#     'Russia': 0,
#     'Turkey': 8
# }
# keys = dct.keys()
# print(keys)
# value = dct.values()
# print(value)

# all = list(dct.items())
# print(all)

# def missing(nums, s):
    # nums = [0, 1, 2]
    # s = "Thnh jjn"
    #
    # one = nums[0]
    # two = nums[1]
    # three = nums[2]
    # x = s[one] + s[two] + s[three]
    # return x
# Code here

# def remove_consecutive_duplicates(s : str) -> str:
#     str = {'dfdf as as as', 'dfdf'}
#     a = set(str)
#     return a

