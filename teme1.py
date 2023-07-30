# 1)Introduceti numele si varsta de la tastatura si afisati mesajul:"nume" are "varsta"ani.
# Folositi functia input() pt a salva inputul userului.

# nume = input("numele este")
# print(nume)
# varsta = input("varsta este")
# print(varsta)
# print(nume , 'are', varsta ,'ani')

# 2)calculati indicele de masa corporala introducand de la tastatura toate inputurile necesare.
# formula : bmi = weight //height[m]^2
# Afisati un mesaj care sa indice gradul de risc.

 # masa = float(input('inserati masa corporala:'))
 # inaltime = float(input('inserati inaltimea:'))
 # bmi = masa(inaltime)**2
 # bmi = mass/(height**2)
 # if IMC < 18.5 :
 #     print("greutate sanatoasa")
 # if 25.00 <= IMC < 29.00:
 #     PRINT("excces de greutate")
 # if IMC >= 30 :
 #     print("obezitate")
#
# 3) Calculati aria si perimetrul unui triunghi dreptunghic care are cele doua catete cu urm valori:
# a = 2
# b = 4
# ip = (a**2 +b**2)**0.5
# print('ipotenuza este :',ip)
# aria = b*a/2
# print('aria este:',aria)
# perimetru = a+b+ip
# print('perimetrul este:',perimetru)

# 4)Scrie un program de la tastatura care citeste 2 numere naturale.
# Daca a >b ,afiseaza a- b.
# Daca a<b ,afiseaza b-a.
# a = int(input('a='))
# b = int(input('b='))
# if a > b :
#     print(a-b)
# else :a < b
# print(b-a)
#
# 5)Introduceti de la tastatura un nr de 3 cifre.
# Daca nr este par ,afisati suma ditre numarul introdus si ultima lui cifra.
# Daca este impar afisati daca este multiplu de 3.

# numarul = input('numarul este:')
# int_nb = int(numarul)
# if len(numarul)==3:
#  if int_nb% 2==0:
#      print(int_nb+int(numarul[-1]))
#  elif int_nb%3 ==0:
#      print('impar si divizibil cu 3')
#  else:
#      print('impar dar nu este divizibil cu 3')
# else:
#     print('numarul nu are 3 cifre')

# 6)Scrie un program care citeste o propozitie de la tastatura.
# Afiseaza nr cuvintelor din acea propozitie.

# prop = input('propozitia este:')
# prop_fara_spatii = prop.strip(prop)
# print(prop_fara_spatii)
# print(prop_fara_spatii.count('')+1)

# 7)Afiseaza pe ecran numele useru-lui din aceste string:

# command='platform: solaris; version: 2.5 ; username: mcristi ; allrights reserved to_'
# ind_1 = command.find('username') + len('username')
# ind_2 = command.rfind(';')
# print(command[ind_1:ind_2])