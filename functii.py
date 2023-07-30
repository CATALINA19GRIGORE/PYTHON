# 1)Extrageti 6 numere randomly utilizand sets

# def extract_numbers(numbers:list)->list[str]:
#     """extracts six numbers from a given list of 49 elements"""
#     numbers = set(numbers)
#     print(numbers)
#     result =((numbers).pop()  for i  in range(6))
#     return result
#
# numbers = list(range(1,50))
# print(numbers)
# str_numbers = [str(i) for i in numbers]
# print(str_numbers)
# result = extract_numbers(str_numbers)
# result1 = extract_numbers(str_numbers)
# result2 = extract_numbers(str_numbers)
# result3 = extract_numbers(str_numbers)
# result4 = extract_numbers(str_numbers)
# print(result)
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# 2) Fie un intreg pozitiv n,dat ca input.
# scrie o aplicatie care sa printeze o forma triunghiulara realizata cu *
# n reprezinta nr de randuri ale acestui pattern.nr de pe fiecare rand va creste cu 2
#
# def triangle(n):
#     """prints a triangle form of characters "*" with n lines"""
#     for i in range(n):
#         print('*' * (2 * i+1))
#     return(triangle(4))
# print(triangle(4))

# 3)Se da un string s.scrie o functie care returneaza suma caracterelor de tip cifra din s.
# modifica functia a i sa returneze suma nr din s.un nr este reprezentant de caractere numerice
# alaturate.
# def adunare_din_string(s: str) -> int:
#         cifre = "1234567890"
#         numar = 0
#         total = 0
#         for ch in cifre:
#             if ch in cifre:
#                 cif = int(ch)
#                 numar = numar *10 + cif
#                 print (numar)
#             else:
#                 total += numar
#                 numar = 0
#         return total

