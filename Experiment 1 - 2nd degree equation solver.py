# It's in portuguese. :s
# Um programa que resolve equações de 2° grau.

# Fórmula básica: x=(-b+-²v(b²-4ac)/(2a)
# Estrutura de fórmula básica ax²+bx+c=0

# 0) Bibliotecas utilizadas

import os

# 1) Inserindo dados

os.system('cls')
a, b, c, confirm, program = 0, 0 , 0, 0, 0
m = ('----------------------------------------------\n Canal de Resolução para equações de 2° grau\n----------------------------------------------\n')
n = ('\nInsira um valor (inteiro) válido para')
o = ('\nInsira os dados.')

while program == 0:

    print (f'{m}{o} (três restantes)\n')

    #########Preencher A
    while confirm == 0:
        while a == 0:
            try:
                a = int(input(f'{n} A: '))
                if a != 0:
                    break
            except ValueError:
                a = 0

        os.system('cls')
        print (f'{m}{o} (dois restantes)\n')
        print (f'\nA = {a}\n...\n')

        #########Preencher B
        while b == 0:
            try:
                b = int(input(f'{n} B: '))
                if b != 0:
                    break
            except ValueError:
                b = 0
        
        os.system('cls')
        print (f'{m}{o} (um restante)\n')
        print (f'\nA = {a}\nB = {b}\n...\n')

        #########Preencher C
        while c == 0:
            try:
                c = int(input(f'{n} C: '))
                if c != 0:
                    break
            except ValueError:
                c = 0
        
        os.system('cls')
        print (f'{m}\nConfirmação dos dados:')
        print (f'\nA = {a}\nB = {b}\nC = {c}\n')


        # 1.2) Confirmação & Edição
        try:
            confirm = input('Tecle ENTER para calcular ou envie qualquer coisa para editar.\n\n')
            if confirm == (''):
                os.system('cls')
                print (f'{m}\nDados:')
                print (f'\nA = {a}\nB = {b}\nC = {c}\n')
                break
            if confirm != (''):
                a, b, c, confirm = 0, 0 ,0 , 0
                os.system('cls')
                print (f'{m}\nInsira os dados novamente.\n\n')

        except ValueError:
            confirm = 0


    # 2) Calculando

    if confirm == (''):
        print ('------- Cálculo -------\n')

    ### Inserção interna e correção de type de dados
    x, delta, raiz = float(0), float(0), float(0)
    a, b, c = float(a), float(b), float(c)
    x1, x2 = float(0), float(0)

    ### Inversão da equação p/ 'a' negativo.
    if a < 0:
        a = a *- 1
        b = b *- 1
        c = c *- 1

    ###Resolução de Delta
    delta = (b)**2 - 4 * a * c
    print (f'Delta: {delta:.2f}\n')

    ### Raiz quadrada
    raiz = delta ** 0.5

    # 3) Exibindo resultado

    ### x1
    print (f'Equação da raíz 1: x1 = ( -({b:.0f}) +({raiz:.2f})) / (2 x {a:.0f})')
    x1 = (-b + raiz) / (2 * a)
    print (f'RAÍZ 1 = {x1:.2f}\n')

    ### x2
    print (f'Equação da raíz 2: x2 = (- ({b:.0f}) -({raiz:.2f})) / (2 x {a:.0f})')
    x2 = (- b - raiz ) / (2 * a)
    print (f'RAÍZ 2 = {x2:.2f}')


    # 4) Despedida & Reincialização

    try:
        program = input('\nPressione ENTER para calcular novamente ou envie qualquer coisa para sair.\n\n')
        if program != (''):
            break
        if program == (''):
            a, b, c, confirm, program = 0, 0 ,0 , 0, 0
            print ('Reiniciando...\n\n')
            os.system('cls')

    except ValueError:
        confirm = 0
