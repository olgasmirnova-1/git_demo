# # # lst = ['Преобразование', 'через', 'метод', 'join()']
# # #
# # # #Объединяем элементы списка с пустым разделителем
# # # print(''.join(lst))
# # # # >>> Преобразованиечерезметодjoin()
# # #
# # # # Устанавливаем пробел в качестве разделителя
# # # print(','.join(lst))
# # # # >>> Преобразование через метод join()
# #
# # def largest_sum(s):
# #     s = "72102450111111090"
# #     lst = []
# #     for item in s:
# #         lst.append(item)
# #         print(lst)
# #     return
# #
# # #
# # #     print(new_l)
# #
# # # def func(*args):
# # #     l =[]
# # #     print(len(args))
# # #     for item in args:
# # #         l.append(item*item)
# # #         print(f'this {l}')
# # #     return
# # #     (l)
# # #
# # #
# # # print(func(2, 5, 8, 10))
# # #
# def compare(a, b):
#     a = 11
#     b = 51
#     c = map(a, b)
#     # print(c)

# a = sorted("This is a test string from Andrew".split(), key=str.endswith("a".))
# print(a)
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

# def number(bus_stops):
#     return sum(i[0] - i[1] for i in bus_stops)
#     bus_stops = [[10, 0], [3, 5], [5, 8]]

    # Good Luck!

# my_list = [[3,4,5],[[9,9,9]],["a,b,c"]]
# , [6, 7, 8, 9, 10, [11, 12]]]
# print(my_list[0:-1]+my_list[-1])
#
# my_list = [1, 2, 3, 4, 5, [6, 7, 8, 9, 10, [11, 12]]]
# my_list.reverse

def flatten(lst):
    r = []
    for x in lst:
       if type(x) is list:
          r.extend(x)
       else:
          r.append(x)
    print(r)
    return r
flatten([[3,4,5],[[9,9,9]],["a,b,c"]])