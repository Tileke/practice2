# Кортеж, цикл for, range

# Tuple -> Кортеж (неизменяемый, упорядочный, итерируемый)

# names = ('John', 'Sam', 'Tolik')
# print(type(names))
# print(names[0])
# print(dir(names))
# count_name = names.count('John')
# print(count_name)
# print(names.index('Sam'))

# for i in names:
#     print(i)

# Цикл исcпользуется в тех случаях, когда нужно повторить что-нибудь n-oe кол-во раз или пройтись интерируемому обьекту. 
 
# for i in range(10):
#     print(i)

# for i in range(5, 11):
#     print(i)

# for i in range(0, 11, 2):
#     print(i)

# l = range(10)
# print(list(l))

# list_ = range(0, 21)
# l1 = []
# l2 = []
# for i in list_:
#     if i % 2 == 0:
#         l1.append(i)
#         print(f'{i} - Четное')
#     else:
#         l2.append(i)
#         print(f'{i} - Нечетное')
    
# break, continue, pass

# for i in range(10):
#     print(i)
#     if i == 5:
#         break # досрочно останавливает цикл 

# for i in rage(10):
#     if i == 5:
#         continue
#     print(i)

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(5):
#     print(i)
# else:
#     print('END')

# list_ = ['Alex', 'John', 'Sam', 'Rachel', 'Tolik']
# for i in list_:
#     if i == 'John':
#         continue
#     print(f'Hi, {i}, you are invited to my b-day')

# list_ = [['John', 22], ['Sam', 11], ['Tolik', 25]]
# for i in list_:
#     if i[1] >= 18:
#         print(f'Welcome, {i[0]}, you are {i[1]} years old. \nYou can come in.')
#     else:
#         print(f'Hello {i[0]}. Come back in {18 - i[1]} years.')
    