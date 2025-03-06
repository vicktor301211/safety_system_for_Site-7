
from pickle import*
from hashlib import*



def hashing_password(text):
    return sha256(text.encode()).hexdigest()

hash_password = "e10c69b90d10a33e36caa8922fba734a54532a0532438bbee4ef19495f1b2158"
password_input = input("Пароль: ")
hash_input_password = hashing_password(password_input)

if hash_password == hash_input_password:
    print("Вход успешен!")
else:
    print("Неверный пароль!")

