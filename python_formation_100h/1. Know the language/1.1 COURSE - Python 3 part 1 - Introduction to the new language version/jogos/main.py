# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

numero_secreto = 42

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    numero_secreto = 42
    total_de_tentativas = 3
    rodada = 1

    while (rodada <= total_de_tentativas):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu número: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Parabéns! Você acertou!")
        else:
            if (maior):
                print("O seu chute foi maior do que o número secreto!")
            elif (menor):
                print("O seu chute foi menor do que o número secreto!")

        rodada = rodada + 1

    print("Fim do jogo")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
