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
        s = input('Caso queria sair do jogo, digite "sair", caso contrario digite "ficar" ?')
        if s == "sair":
            aposta = False
            game = False
            print('Até mais!')
        a = input('Você gostaria de aposta: Pass Line (P), Field (F), Any Craps (A) ou Twelve  (T), por favor escolha um de cada vez!')
        if a == 'P':
            tipos.append(a)
            bet = int(input('Quanto quer apostar em Pass Line?'))

