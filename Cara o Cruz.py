import random

def double_letter(text):
    result=''
    for l in text: result+=l*2
    return result

def secret_function(a,b):
    r=str(a)+str(b)
    return "¡"+r if isinstance(a,str) and isinstance(b,str) else r

def coin_flip(): return random.choice(["Cara","Cruz"])

print(secret_function(1,2))
print(secret_function("Hola, ","Mundo!"))
print("Moneda:",coin_flip())
