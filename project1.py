import random

a =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

gener_password = ""

password_len = int(input('Введите длину пароля: '))

for i in range(password_len):
    gener_password += random.choice(a)
print(gener_password)
