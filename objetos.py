from random import randint

class Personagem:
    def __init__(self, nome, saude, energia, ataque, defesa):
        # Atributos / Propriedades
        self.nome = nome
        self.saude = saude
        self.energia = energia
        self.ataque = ataque
        self.defesa = defesa

    # Métodos
    def atacar(self):
        self.energia = self.energia - 10
        return randint(0, self.ataque)

    def defender(self):
        self.energia = self.energia - 5
        return randint(0, self.defesa)

    def descansar(self):
        self.energia = 100

    def golpeEspecial(self):
        return int(((self.ataque + self.defesa) / 2) * 3)

personagem1 = Personagem('Aragorn', 100, 100, 90 , 70)

print(personagem1.energia)
print(personagem1.golpeEspecial())

