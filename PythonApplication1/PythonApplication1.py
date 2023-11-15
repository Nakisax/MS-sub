
import random

letters = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i",
           "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r",
           "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "=", "-", "+", ";", ":", "*", "{", "}", "[", "]"]


how_many_letters = int(input("How many letter do you want in your password? "))
how_many_numbers = int(input("How many numbers do you want in your password? "))
how_many_symbols = int(input("How many symbols do you want in your password? "))


password = [] 

#symbols from the lists above and append it into the empty list above#

for n1 in range(1, how_many_letters+1):
    password += random.choice(letters)
for n2 in range(1, how_many_numbers+1):
    password += random.choice(numbers)
for n3 in range(1, how_many_symbols+1):
    password += random.choice(symbols)


random.shuffle(password)


passwords = ""
for char in password:
    passwords += char

print("New generated password: {passwords}")   