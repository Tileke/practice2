# Создание листов (списков)
# list_= [] # Литералы 
# list_ = [1, True, [1, 2, 3], 'hello']
# list_[-1] = 'Makers'
# print(list_)

# lst = [1, 2, 3, 4, 5, 9]
# lst2 = [1, 2, 3, 4, 5, 7, 5]
# print(lst < lst2)

# list()
# a = list([1, 2, True])
# print(type(a))

# Основные методы листов
# append() -> добавляет элеементы в список (в конец списка)
# list_ = [1, 2, True]
# inp = input('Enter value: ')
# list_.append(inp)
# print(list_)

# range(start, end, step) 
# ls = list(range(11))
# print(ls)

# for
# list_ = [1, 3, True, 9, False]
# for i in list_:
#     print(i)

# ls = []
# for i in range(11):
#     ls.append(i)
#     print(i)
# print(ls)

# extend() -> Расширяет список добавляя в конец все элементы указанного списка
# ls1 = [1, 'Hello']
# ls2 = [2, 'World']
# ls1.extend(['Makers', 2, 5, 3])
# print(ls1)
# print(ls2)
# print([7, 4, 'Hello'] * 2)

# insert(index, element) Добавляет элемент в указанный индекс 
ls = [1, 3, 4, 5]
ls.insert(1, 2)
print(ls)

# remove(element) Удаляет элемент списка (только первый попавший)

# l = ['h', 2, 'wqr', 8, 'hello', 'h', 'a', 'h', 7]
# ls = []
# for i in l:
#     if type(i) == int:
#         ls.append(i)
# print(ls)

# pop([i]) -> Удаление i-го элемента. Возвращает удаленный элемент. Если индекс не указан, удаляет последний элемент.
# lst = [1, 'go', 'let', 4, True]
# print(lst.pop())
# print(lst)

# index(element, [start, end]) -> Возвращает положение (индекс) элемента (в указанном диапазоне)
# ls = [1, 5, 6, 523, 32, 21, 121, 69, 420, 1337, 1, 4, 1, 121]
# print(ls.index(121, 1, 100))

# count(element) -> Возвращает количество элементов в списке
# ls = ['h', 'e', 'l', 'l', 'o']
# print(ls.count('l'))

# sort(reverse = True, key=функция) -> Сортирует список на основе какой-то функции
# ls = [2, 5, 6, 1, 7, 3, 4]
# ls.sort()
# print(ls)

# ls = ['a', 'h', 'b', 'c', 'o']
# ls.sort()
# print(ls)

# ls = ['aadf', 'hs', 'b', 'caaaa', 'oessss']
# # ls.sort(key=len)
# # print(ls)
# ls.sort(reverse=True, key=len)
# print(ls)

# reverse() - Переворачивает список
# ls.reverse()
# print(ls)

# split(разделитель) - Преобразовывает строку в список по разделителю (split() = ' ')
# a = input('Enter words through space: ')
# b = a.split()
# print(b)

# ''.join(list) - Преобразовывает строку в список
# ls = ['hello', 'world']
# a = ' '.join(ls)
# print(a)

# copy() = Поверхностное копирование
# ls = [1, 3, 5, 6, 7, 9, [1,213,12,21]] 
# ls2 = ls.copy()
# ls2[-1].append(0)
# print(ls, ls2)

# import copy - Копи для хакеров
# ls = [1, 2, 4, [1, 3, 5, 7]]
# ls2 = copy.deepcopy(ls)
# ls2[-1].append(0)
# print(ls2)
# print(ls)

# clear() - Очищает список
# ls = [1, 2, 4, 5, 6]
# print(ls)
# ls.clear()
# print(ls)

