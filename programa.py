def linha():
    print('-' * 40)


def bemvindo():
    linha()
    print('''
    BEM VINDO A CALCULADORA 
    ''')
    linha()
bemvindo()


def calcular():
    # pedir o numero para fazer a conta
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))

    # escolher como somar
    operacao = input('''Digite como deseja fazer a conta:
        + para somar
        - para subtrair
        x para multiplicar
        / para dividir
        ''')
    linha()
    # adição
    if operacao == '+':
        print(f'{num1} + {num2} = ', num1 + num2)

    # subtração
    elif operacao == '-':
        print(f'{num1} - {num2} = ', num1 - num2)

    # multiplicação
    elif operacao == 'x':
        print(f'{num1} x {num2} = ', num1 * num2)

    # divisão
    elif operacao == '/':
        print(f'{num1} / {num2} = ', num1 / num2)

    # caso não tenha definido o operador
    else:
        print("Você não digitou um operador válido, tente rodar o programa novamente.")
    linha()

    # função rodar novamente
    novamente()

#  definindo a função rodar novamente
def novamente():
    calcular_denovo = input('''Deseja Rodar o Programa Novamente? 
    Aperte s para SIM e n para NÂO.''')

    # se quisser somar novamente
    if calcular_denovo == "s":
        bemvindo()
        calcular()

    # caso queira finalizar
    elif calcular_denovo == "n":
        linha()
        print("Programa Finalizado.")
        linha()
    else:
        novamente()

calcular()