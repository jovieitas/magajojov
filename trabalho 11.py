import random

def adivinhe_o_numero():
    numero_aleatorio = random.randint(1, 100)
    tentativas = 0
    acertou = False
    print("Adivinhe o número entre 1 e 100")

    while not acertou:
         palpite = int(input("Digite seu palpite: "))
         tentativas += 1
         if palpite < numero_aleatorio:
             print("Muito baixo!")
         elif palpite > numero_aleatorio:
             print("Muito alto!")
         else:
             print(f"Você adivinhou em {tentativas} tentativas.")
             acertou = True
#adivinhe_o_numero()

import random
def sorteio_premios():
    premios = ["Carro", "Viagem", "Notebook", "Smartphone"]
    participante = input("Digite seu nome: ")
    premio = random.choice(premios)
    print(f"Parabéns, {participante}! Você ganhou um(a) {premio}.")
#sorteio_premios()

import random

def lancar_dado():
    resultado = random.randint(1, 6)
    return resultado

# Teste da função
resultado_do_lancamento = lancar_dado()
print("O resultado do lançamento do dado é:", resultado_do_lancamento)
