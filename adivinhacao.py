import random

def jogar_adivinhacao():
    print('*********************************')
    print('Bem vindo ao jogo de adivinhação')
    print('*********************************')

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 100

    print("Qual o nivel de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("Define o nivel: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Voce digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("você errou! O seu chute foi maior do que o numero secreto.")
            elif (menor):
                print("O seu chute foi menor do que o numero secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos



    print('**** Fim do jogo ****')

    nome = "Nico"
    sobrenome = "Steppat"
    print(nome, sobrenome, sep=" ")

if(__name__ == '__main__'):
    jogar_adivinhacao()