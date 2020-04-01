import random
saldo = 500
game = True
while game:
    aposta =True
    tipos = []
    P = 0
    F = 0
    A = 0
    T = 0
    while aposta:
        print('Seu saldo atual: {0}'.format(saldo))
        print('Você está na rodada "Come out" do jogo! ')
        #tipos possiveis de apostas:
        a = input('Você gostaria de apostar: Pass Line (p), Field (f), Any Craps (a) ou Twelve (t)? Por favor escolha um de cada vez!\n(Caso queria sair do jogo, digite "sair")')
        while a != 'p' or 'f' or 'a' or 't' or 'sair':
            a = input('Inválido! Digite alguma das opções: "p", "f", "a", "t" ou "sair"')
        if a == "sair":
            aposta = False
            game = False
            print('Até mais!')
        elif a == 'p':
            tipos.append(a)
            bet = int(input('Quanto quer apostar em Pass Line?'))
