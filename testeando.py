from random import randint

class NumeroAleatorio:
    def __init__(self):
        self.numero = randint(0,10)

if __name__ == "__main__":
    n = NumeroAleatorio()
    print(n.numero)
    print("Tudo okay!")

# Tudo okay
