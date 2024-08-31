import random

def gen_pass(a):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(a):
        password += random.choice(elements)
    return password
