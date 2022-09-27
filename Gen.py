import random

login = input("Enter your login: \n")
password = ""
lenght = int(input("Enter password lenght: \n"))
answerbool = True
answlist = ["y", "n"]

while answerbool:
    answer = input("Use special charater?: y/n \n")
    if answer not in answlist:
        print("Incorrect answer!")
    elif answer in answlist:
        answerbool = False

liblistws = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
             "q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
             "a", "s", "d", "f", "g", "h", "j", "k", "l", "z",
             "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R",
             "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F",
             "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B",
             "N", "M", "~", "!", "@", "$", "%", "^", "&", "*", "(", ")"]
liblist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
           "q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
           "a", "s", "d", "f", "g", "h", "j", "k", "l", "z",
           "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R",
           "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F",
           "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B",
           "N", "M"]

if answer == "y":
    for i in range(lenght):
        password = password + random.choice(liblistws)
elif answer == "n":
    for i in range(lenght):
        password = password + random.choice(liblist)

print(f"Login:", login, "\nPassword:", password, "\n")
