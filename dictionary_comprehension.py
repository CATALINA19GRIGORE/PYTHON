# 1)Afisati de cate ori apare fiecare caracter dintr -un cuv folosind dict .compreh.

# word = input('word:')
# single_chars = set(word)
# print (single_chars)
# d = {i:word.count(i)for i in word}
# print(d)

# 2)Afisati daca numerele dintr o lista sunt mai mari decat 10 folosind dict.compreh.
# numbers = [1,2,3,5,400,500]
# d = {element:False if element<10 else True for element in numbers}
# print(d)

# 3)Se da o lista de numere .Transforma intregii in stringuri folosind list compreh.
# numbers = [50,9,100,3,33,'@$%&*']
# numbers_as_strings = {str(item)if isinstance (item,int)else item for item in numbers}
# print(numbers_as_strings)

# 4)Afiseaza o lista cu toate patratele perfecte intre 0 si 100,folosind list.compreh.
# patrate_perfecte = [pow(element,2)for element in range(0,101)if element **2<100]
# print(patrate_perfecte)

# 5)Afisati care sunt consoanele dintr un string introdus de la tastatura folosind seturi.
# string = input('introduceti un cuvant de la tastatura:')
# string = set(string)
# vowels = ['a','e','i','o','u']
# consoane = string - set(vowels)
# print(consoane)