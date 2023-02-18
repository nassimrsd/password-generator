import random

lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()."

string = lowerCase + upperCase + numbers + symbols

length = int(input("how many characters should your password contain?  (More than 8 characters is recommended)\n"))

password = "".join(random.sample(string,length))

print("password:\n" + password)