# Лекция: Логические выражения и опрераторы Python (if). NoneType. Условные операторы 

#boolean - неизменяемый тип данных

#True (1)
#False (0)

# print(bool(1))
# print(bool(0)) #False
# print(bool(0.1))
# print(bool(-1000))
# print(bool('hello')) 
# print(bool('')) #False
# print(bool[1,2,3]))
# print(bool[])) #False

# NoneType - это ничего (нейтральное значение)

# None 
# val = None
# print(type(val))
# print(bool(None)) # False

# print(5 > 2) #True
# print(5 < 2) #False
# print(5 >= 2) #True
# print(5 >= 6) #False
# print(5 == 5) #True
# print(5 <= 5) #True
# print(5 <= 6) #True
# print(5 <=3) #False
# print(5 == 5) #True
# print(5 != 5) #False
# print(6 != 5) #True

# s = 'hello'
# print('e' in s)
# print('ll' in s)
# print('hl' in s)

# print(True == False and True == True) #False
# print(5 > 2 and 5 > 6) #False
# print(True == True and 5 == 5) #True
# print(True == True and True == True and False == True) #False

# print(True or False) #True
# print(5 > 2 or 5 > 6) #True
# print(5 > 2 or 5 > 3) #True
# print(5 < 2 or 5 > 3) #True
# print(True == True and False == False or 5 > 2) #True 
# print(2 + 2 * 2) #6
# print((2+2) * 2) #8

# print(not True) #False
# print(not False) #True
# print((not False) == True and (not True) == (not False)) #False

# Условные операторы (if)

# if 5 < 2: #False
#     print('Если')
# else:
#     print('Иначе')
# (print('Конец'))

# a = 2
# b = 3
# if a > b:
#     print('a is bigger')

# a = 3
# b = 3
# if a > b:
#     print('a is bigger')
# elif a == b:
#     print('a equals b')
# else: 
#     print('b is bigger')

# num = int(input('Enter a number between 1-5: '))
# if num == 5: 
#     print('Your number is 5')
# elif num == 4: 
#     print('Your number is 4')
# elif num == 3: 
#     print('Your number is 3')
# elif num == 2: 
#     print('Your number is 2')
# elif num == 1: 
#     print('Your number is 1')
# else:
#     print('You enter a wrong number dumbass')

# num = int(input('Enter a number between 1-5: '))
# if num > 5 or num < 1:
#     print('Wrong number dumbass')
# print(f'Ur number is {num}')

