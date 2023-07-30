# 1)Afisati toate numerele pare intre 0 si 3000.

# for i in range(2,3001,2):
#     print(i)

# for i in range(2,3001):
#   if i % 2 ==0:
#     print(i)

# 2)Afisati toate nr. prime intre 0 si 1000.
# a = 0
# b = 1000
# print("numerele prime intre 'a' si 'b' sunt:")
# for num in range(a,b+1):
#     if num>1:
#         for i in range (2,num-1):
#             if num % 1==0:
#                 break
#     else:
#         print(num)

# 3)Afisati cate vocale contine un text pe care il introduceti de la tastatura .
# Afisati si numarul consoanelor.

# propozitie = input('propozitie:').lower()
# vocale = 'aeiouAEIOU'
# v = 0
# c = 0
# for char in propozitie:
#     if char in 'aeiouAEIOU':
#         v+=1
#     elif char.isalpha():
#        c == 1
# print(f'numarul vocalelor este:{v},iar numarul consoanelor este {c}')

# 4)Se introduc 2 stringuri .
# Cate caractere comune au.

# text_1 = input('text_1:')
# text_2 = input('text_2:')
# ch = "".count('ch')
# for ch in text_1:
#     if ch in text_2:
#         print(f'{ch} este comun:')

# 5)Se introduce de la tastatura o propozitie .
# Afisati stringul din caractere distincte.
# prop = input('propozitie:')
# comune = ''
# for item in prop:
#     if prop.count(item)>= 1:
#      if item not in comune:
#         comune += item
# print(comune)

# 6)Introduceti de la tastatura un nr natural n.Calculat n!,afisand rezultatul
# 4!=1*2*3*4
# 9!=1*2*3*4*5*6*7*8*9

# number = input('number:')
# n = 1
# for i in range(1, int(number)+1):
#     n = n*i
# print(n)