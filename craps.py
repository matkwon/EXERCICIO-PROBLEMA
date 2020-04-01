import random
saldo = 500
game = True
while game:
    aposta =True
    tipos = []
    p = 0
    f = 0
    a = 0
    t = 0
    while aposta:
        print('Seu saldo atual: {0}'.format(saldo))
        print('Você está na rodada "Come out" do jogo!')
        #tipos possiveis de apostas:
        a = input('Você gostaria de apostar: Pass Line ("p"), Field ("f"), Any Craps ("a") ou Twelve ("t")? Por favor escolha um de cada vez!\n(Caso queria sair do jogo, digite "sair")\n')
        while a != 'p' or 'f' or 'a' or 't' or 'sair':
            a = input('Inválido! Digite alguma das opções: "p", "f", "a", "t" ou "sair"\n')
        if a == "sair":
            aposta = False
            game = False
            print('Até mais!')
        elif a == 'p':
            tipos.append(a)
            bet = int(input('Quanto quer apostar em Pass Line?\n'))
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

