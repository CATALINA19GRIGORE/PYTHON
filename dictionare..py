# 1)Se dau urmatoarele liste:
# employees = ['Michal', 'Harry', 'Susan', 'Dan' ,'Christen']
# email = ['michal@comp.com' , 'harry@comp.com' , 'susan@comp.com'
# , 'dan@comp.com' , 'christen@comp.com']
# Scrie un program care adauga intr un dictionar perechile cheie valoare,reprezentate de elementele din lista.
# care vor fi cheile

# employees = ['Michal', 'Harry', 'Susan', 'Dan' ,'Christen']
# email = ['michal@comp.com' , 'harry@comp.com' , 'susan@comp.com'
# , 'dan@comp.com' , 'christen@comp.com']
# d = {}
# print(tuple(enumerate(email)))
# for i , email in enumerate(email):
#     d[email]=employees[i]
#     print(d)

# 2)Se da un dictionar cu notele de la matematica ale unor elevi,notele fiind valori.\
# Afisati elevul/elevii cu noata maxima.

# math_grades = {'Marius':8.00,'Andreea':9.5, 'Adrian':7.9, 'Bianca':10}
# s = sum(math_grades.values())
# media = s/len(math_grades)
# print(media)
# m = max(math_grades.values())
# elevi = []
# for k,v in math_grades.items():
#     if v ==m:
#         elevi.append(k)
# print(elevi)
# print(f'numarul elevilor cu nota maxima este:{len(elevi)}')

# 3)Se da urmatorul dictionar:
# Modificati salariul unui angajat pe baza id-ului de angajat introdus de la tastatura
# Daca id ul nu este al unui angajat se va cere reintroducere.
# Noul salariu se introduce de la tastatura

# employee = {1:{'name':'Andrei' ,'salary' :100},2:{'name':'Vlad','salary':500},
# 3:{'name':'ioana','salary':330}}
# empl_id = (input('introduceti id:'))
# while empl_id not in employee.keys():
#     empl_id = int(input('enter the id:'))
# new_salary = input('insert salary:')
# empl = employee[empl_id]
# empl['salary']=int(new_salary)
# print(employee)
#
# 4)Afisati de cate ori apare fiecare intreg din urmatoarea lista:

# numbers=[1,1,3,7,9,2,3,100,9,333,2.0,5,1,3,3]
# d = {}
# for num in numbers:
#     d[num]=numbers.count(num)
# print(d)