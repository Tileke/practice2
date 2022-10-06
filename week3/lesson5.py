# counting specific letters

# text = 'The little brown fox jumps over the lazy dog'
# result1 = text.lower().count('t')
# print(result1)

# result2 = 0
# for ch in text.lower():
#     if ch == 't':
#         result2 += 1
# print(result2)

# text = 'The little brown fox jumps over the lazy dog' 
# result1 = text.isupper()
# print(result1)


# Find out if the string is (.isupper()) without using .isupper()
# big_letters = []
# for i in range(ord('A'), ord('Z')+1):
#     big_letters.append(i)   
# result = None
# text = 'JFK AAPL' 
# for ch in text:
#     if ch == ' ':
#         continue
#     if ord(ch) not in big_letters:
#         result = False
#         break
#     else:
#         result = True
# print(result, text.isupper())

# print every letter from a list (if l, don't print it)
# sentence = ['hello', 'world']
# for word in sentence:
#     print(word)
#     for i in word:
#         if i == 'l':
#             break
#         print(i)

# list_ = ['hello', 'world']
# list_.reverse()
# print(list_)

# list_ = ['hello', 'world']
# list_.reverse()
# print(list_)

# suitcase = []
# suitcase.append('shirt')
# suitcase.append('shorts')
# suitcase.append('pants')
# suitcase.append('slides')
# suitcase.append('glasses')
# suitcase.pop(-1)
# print(suitcase)

# a = int(input('')).replace(',', '')
# list_ = []
# for i in list_:
#     list_.append(i)



a = input('')
list_ = a.split(',')
list_ = sorted(list_)
print(list_)
