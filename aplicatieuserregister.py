# Creeaza o aplicatie care permite user registration (first name,last name,user,password,email.)
# si user login .Bazele de inregistrare se salveaza intr un fisier csv .
# Utilizatorul se poate loga doar daca s a inregistrat .
# Dupa logare userul are posibilitatea de afisare detalii -> first name,last name ,email .
# Optiunea de afisare detalii nu apare inainte de logare .

# def menu():
#     """
#     the user chose a valid option from the meniu
#
#     """
#     print ('1.register:\n 2.login:\n3.exit')
#     return input('please chose:')
#
# def register_user_(username ,userpass,name,email):
#     """
# this function registring the user and append the username ,userpass,name ,email in data_csv if aren' t there
#
#     """
#     with open('data_csv','a',newline='')as file:
#         writer = csv.writer(file)
#         writter.writerow([username,userpass,name,email])
#     print('are register succesfully')
#
# def login_user_(username,password):
#     """the function give de permision to login for all the username that are registring
#     """
#     with open('data_csv.csv','r',newline='')as fr:
#         reader = csv.reader(fr)
#         for row in reader:
#             if username in row and password in row:
#                 print('succesfullylogged in')
#                 print(f'userul:{username},name :{name},email:{email}succesfully loggin')
#                 break
#             else:
#                 print('the user doesn\' t exist!please register in!')
#                 menu()
#
# if__name__='__main__'
# while True:
#         option = menu()
#         if option == '1':
#             username = input('username:')
#             userpass = input('password:')
#             name = input('name:')
#             email = input('email:')
#             register_user (username,userpass,name,email )
#         elif option == '2':
#             username = input('username:')
#             password == input('password:')
#             login_user(username,passwd)




