# 1)Se citeste un numar intreg de 4 cifre,afisati care este urmatorul numar de 4 cifre
# ,cu toate cifrele distincte,folosind seturi.
# varianta 1

# n = input('introduceti nr:')
# n_int = int(n)
# rezultat = n_int + 1
# while True:
#     r_str = str(rezultat)
#     for ch in r_str:
#         if r_str.count(ch)>1:
#             break
#         else:
#             print(rezultat)
#             break
#         rezultat +=1

#  varianta 2

# n = input('n=')
# n = str(int(n)+1)
# while len(n)!=len(set(n)):
#     n = str(int(n)+1)
# print(n)

# 2)Jocul 6/49

# numbers = range(1,50)
# str_numbers = set(map(str,numbers))
# print(str_numbers)
# for _ in range(6):
#     print(str_numbers.pop())

# 3)Se dau listele:
# Care sunt angajatii care au si card combustibil si abonament la sala ?
# Care sunt angajatii care nu au nici card combustibil nici abonament la sala?

# angajati = ['Marius' ,'Andrei','Bianca','Ana','Mihai']
# card_combustibil = ['Maria','Andrei']
# abonament_sala = ['Maria','Andrei','Mihai']
# result = set(card_combustibil).intersection(abonament_sala)
# print(result)
# result_2 = set(angajati).difference(card_combustibil,abonament_sala)
# print(result_2)

# 4)Eliminati duplicatele din cadrul unui cuvant introdus de la tastatura.


# 5)Se dau doua liste.Afisati care sunt elementele lor comune,afisati si elementele diferite.

# lista_1 = list(input('introduceti lista1:'))
# lista_2 = list(input('introduceti lista2:'))
# commun_elements = set(lista_1).intersection(lista_2)
# print(commun_elements)
# differit_elements = set(lista_1).difference(lista_2)
# print(differit_elements)



