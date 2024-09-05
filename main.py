import random

charst = "abcdefghijklmnopqrstuvwryzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!@#$%^&*(){}[]()"
lenth = int(input("enter lenth of your password: "))
password = ""

for a in range(lenth):
    password += random.choice(charst)

print(password)