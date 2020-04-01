import random
saldo = 500
game = True
while game:
    aposta =True
    tipos = []
    p = 0
    f = 0
    c = 0
    t = 0
    while aposta:
        print('Seu saldo atual: {0}'.format(saldo))
        print('Você está na rodada "Come out" do jogo!')
        #tipos possiveis de apostas:
        a = input('Você gostaria de apostar: Pass Line ("p"), Field ("f"), Craps ("c") ou Twelve ("t")? Por favor escolha um de cada vez!\n(Caso queria sair do jogo, digite "sair")\n')
        while a != 'p' or 'f' or 'c' or 't' or 'sair':
            a = input('Inválido! Digite alguma das opções: "p", "f", "c", "t" ou "sair"\n')
        if a == "sair":
            aposta = False
            game = False
            print('Até mais!')
        elif a == 'p':
            tipos.append(a)
            bet = int(input('Quanto quer apostar em Pass Line? (1:1)\n'))
            while bet > saldo or bet < 0:
                bet = input('Aposte um valor que você CONSIGA apostar! Seu saldo atual: {0}\n'.format(saldo))
            p += bet
            saldo -= bet
            print('Saldo: {0}'.format(saldo))
            fim = input('Você deseja continuar as apostas ("a") ou rolar os dados ("d")?\n')
            while fim != 'a' and 'd':
                input('Escolha inválida! "a" ou "d".\n')
            if fim == 'd':
                aposta = False
        elif a == 'f':
            tipos.append(a)
            bet = int(input('Quanto quer apostar em Field? (1:1) ou (2:1, se somar 2) ou (3:1, se somar 12)\n'))
            while bet > saldo or bet < 0:
                bet = input('Aposte um valor que você CONSIGA apostar! Seu saldo atual: {0}\n'.format(saldo))
            f += bet
            saldo -= bet
            print('Saldo: {0}'.format(saldo))
            fim = input('Você deseja continuar as apostas ("a") ou rolar os dados ("d")?\n')
            while fim != 'a' and 'd':
                input('Escolha inválida! "a" ou "d".\n')
            if fim == 'd':
                aposta = False
        elif a == 'c':
            tipos.append(a)
            bet = int(input('Quanto quer apostar em Craps? (7:1)\n'))
            while bet > saldo or bet < 0:
                bet = input('Aposte um valor que você CONSIGA apostar! Seu saldo atual: {0}\n'.format(saldo))
            c += bet
            saldo -= bet
            print('Saldo: {0}'.format(saldo))
            fim = input('Você deseja continuar as apostas ("a") ou rolar os dados ("d")?\n')
            while fim != 'a' and 'd':
                input('Escolha inválida! "a" ou "d".\n')
            if fim == 'd':
                aposta = False
        elif a == 't':
            tipos.append(a)
            bet = int(input('Quanto quer apostar em Twelve? (30:1)\n'))
            while bet > saldo or bet < 0:
                bet = input('Aposte um valor que você CONSIGA apostar! Seu saldo atual: {0}\n'.format(saldo))
            t += bet
            saldo -= bet
            print('Saldo: {0}'.format(saldo))
            fim = input('Você deseja continuar as apostas ("a") ou rolar os dados ("d")?\n')
            while fim != 'a' and 'd':
                input('Escolha inválida! "a" ou "d".\n')
            if fim == 'd':
                aposta = False
    while jogo:
        dado1 = random.randint(1,6)
        print('Dado 1: {0}'.format(dado1))
        dado2 = random.randint(1,6)
        print('Dado 2: {0}'.format(dado2))
        print('Soma: {0}'.format(dado1+dado2))