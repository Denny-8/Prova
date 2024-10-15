import random

string = "abcdefghijklnopqrstuvwxyz0123456789"

n = int(input("inserire lunghezza della password"))
password = ""

for i in range(n):
    password += random.choice(string)

print("La password generata è", password)
