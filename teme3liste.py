# 1)Afisati cel mai mare numar dintr o lista.Lista poate sa contina orice tip de date.
# lista = [1, "Pyhton",2.5,15,["a","b",20],5.5]
# numere=[]
# for n in lista:
#     if isinstance(n, int) or  isinstance(n,float):
#         numere.append(n)
# print(numere)
# nr_max = max(numere)
# print("cel mai mare numar din lista este:" ,nr_max)

#     varianta 2
# numbers = [10,5,25,15,30,20]
# nr = numbers[0]
# for num in numbers:
#     if num > nr:
#         nr = num
# print('cel mai mare numar este:', nr)

# 2)Eliminati dintr o propozitie data ca input toate cuvintele care incep cu A,a.
# Afisati propozitia fara acele cuvinte.

# propozitie = input('introduceti o propozitie:')
# propozitie = propozitie.lower()
# lista_cuvinte = propozitie.split()
# print(lista_cuvinte)
# lista_2 = []
# for cuvant in lista_cuvinte:
#     if not cuvant.startswith("a"):
#         lista_2.append(cuvant)
# print(lista_2)
# propozitie_rezultata = "".join(lista_2)
# print(propozitie_rezultata)
#
# 3)Se da o lista de cuvinte(stringuri).Afiseaza o lista in care cuvinteledin lista data ca input sunt scrie invers
# de la dreapta la stanga .

# words = ['python','ruby','javascript']
# lista_noua = []
# for i in words :
#     item = i in words
#     item = i [::-1]
#     lista_noua.append(item)
# print(lista_noua)

# 4)Se citeste un nr de la tastatura de 4 cifre.Afisati care este urm nr de 4 cifre,cu toate
# cifrele distincte.
# n = input('nr:')
# print(n)
# nr = int(n)+1
# print(nr)
# while nr:
#     for item in str(nr):
#         if str(nr).count(item)>1:
#             break
# else:
#     print(f'{nr}are toate cifrele distincte')

# 5)Se da o lista de cuvinte.
# Afisati cuv care au un nr de caractere mai mare decat valoarea medie a carcaterelor din lista
#
words = ['curajos' , 'curat' , 'custodie' , 'copilarie']
# big_words = []
# suma_len = 0
# suma_len = len(''.join(words))
# print(f'suma_len ={suma_len}')
# avg_len = suma_len/len(words)
# print(f'valoarea medie a caracterelor este{avg_len}')

# cu list compreh

# words = ['curajos' , 'curat' , 'custodie' , 'copilarie']
# suma_len = 0
# suma_len = len(''.join(words))
# print(suma_len)
# avg_len = (suma_len)/len(words)
# big_words = [item for item in words if len(item)>avg_len]
# print(f'cuvintele care au un nr mai mare decat valoarea medie a carac din lista'
#       f' sunt{big_words}')

# 6)Adaugati intr o lista toate numerele de la 0 la 10 ,inmultite cu 3.

# lst = []
# for i in range(11):
#     lst.append(i*3)
# print(lst)

# cu list compreh

# lst = [i*3 for i in range(11)]
# print(lst)

# 7) Adaugati toate nr impare care se afla intre 0 si 100 ,intr o lista

# lst = []
# for i in range(100):
#     if i % 2 != 0:
#         lst.append(i)
#         print(lst)



# 8)adaugati intr o lista persoanele care au peste 18 ani.

# persoane = [('Bogdan', 14) ,('Ana',20),('Marius',18),('Ionut',30)]
# new_persoane =[]
# for nume,varsta  in persoane:
#     if varsta >=18 :
#         new_persoane.append(nume)
#         print(new_persoane)




