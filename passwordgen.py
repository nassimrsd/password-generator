import random
import os

lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()."
i = ""
while i != "x":
    os.system('clear')
    string = lowerCase + upperCase + numbers + symbols
    length = int(input("How many characters should your password contain?  (More than 8 characters is recommended)\n"))
    password = "".join(random.sample(string,length))
    print("password:\n" + password)
    choice = input("Do you want your password saved in passwords.txt yes/no\n")

    if choice == "yes" or choice == "Yes":
        name = input("Give your password text file a name\n")
        file = open(f"passwords/{name}.txt","w")
        file.write(f"Name:{name}\nPassword:{password}")

    i = input("Enter 'x' to quit")

    
    
    