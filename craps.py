#Design de Software - Exercício Problema
#Jogo de Craps simplificado
#Produzido por:
#Matheus Kwon
#Vitor Fortes Giuliano Riccetti


import random
#saldo inicial:
saldo = 500
game = True
while game:
    aposta = True
    point = False
    #guarda os tipos de apostas:
    tipos = []
    #variáveis que guardam as apostas de cada tipo na rodada come out :
    p = 0
    f = 0
    c = 0
    t = 0
    while aposta:
        print('Seu saldo atual: {0}'.format(saldo))
        print('Você está na rodada "Come out" do jogo!')
        #tipos possíveis de apostas:
        a=input('Você gostaria de apostar em: Pass Line ("P"), Field ("F"), Craps ("C") ou Twelve ("T")? Por favor escolha um de cada vez!\n'  
        '(Caso queria sair do jogo, digite "SAIR")\n')
        if a!= 'P' and a!='F' and a!='C' and a!='T' and a!="SAIR":
            invalida=True
            while invalida:
                a=input('Escolha inválida! Selecione: "P" para Pass Line, "F" para Field , "C" para Craps ou "T" para Twelve. Caso queira sair escreva "SAIR": ')
                if a=='P' or a=='F' or a=='C' or a=='T' or a=="SAIR":
                    invalida=False
                else:
                    invalida=True
        if a == "SAIR":
            aposta = False
            game = False
            print('Até mais!')
        #condicionamentos de cada escolha de aposta:
        elif a == 'P':
            #aposta atual:
            bet = int(input('Quanto quer apostar em Pass Line? (1:1)\n'))
            while bet > saldo or bet < 0:
                bet = int(input('Aposte um valor que você CONSIGA apostar! Seu saldo atual: {0}\n'.format(saldo)))
            p += bet
            saldo -= bet
            print('Saldo: {0}'.format(saldo))
            if saldo == 0:
                print('Você não tem mais dinheiro para apostar nessa rodada.')
                input('Aperte ENTER para jogar os dados')
                aposta = False
            else:
                fim = input('Você deseja continuar as apostas ("CONTINUAR") ou rolar os dados ("JOGAR")?\n')
                while fim!="CONTINUAR" and fim!="JOGAR":
                    fim=input('Escolha inválida! "CONTINUAR" ou "JOGAR".\n')
                if fim == "JOGAR":
                    aposta = False
        elif a == 'F':
            bet = int(input('Quanto quer apostar em Field? (1:1) ou (2:1, se somar 2) ou (3:1, se somar 12)\n'))
            while bet > saldo or bet < 0:
                bet =int(input('Aposte um valor que você CONSIGA apostar! Seu saldo atual: {0}\n'.format(saldo)))
            f += bet
            saldo -= bet
            print('Saldo: {0}'.format(saldo))
            if saldo == 0:
                print('Você não tem mais dinheiro para apostar nessa rodada.')
                input('Aperte ENTER para jogar os dados')
                aposta = False
            else:
                fim = input('Você deseja continuar as apostas ("CONTINUAR") ou rolar os dados ("JOGAR")?\n')
                while fim!="CONTINUAR" and fim!="JOGAR":
                    fim=input('Escolha inválida! "CONTINUAR" ou "JOGAR".\n')
                if fim == "JOGAR":
                    aposta=False
        elif a == 'C':
            bet = int(input('Quanto quer apostar em Craps? (7:1)\n'))
            while bet > saldo or bet < 0:
                bet =int(input('Aposte um valor que você CONSIGA apostar! Seu saldo atual: {0}\n'.format(saldo)))
            c += bet
            saldo -= bet
            print('Saldo: {0}'.format(saldo))
            if saldo == 0:
                print('Você não tem mais dinheiro para apostar nessa rodada.')
                input('Aperte ENTER para jogar os dados')
                aposta = False
            else:
                fim = input('Você deseja continuar as apostas ("CONTINUAR") ou rolar os dados ("JOGAR")?\n')
                while fim!="CONTINUAR" and fim!="JOGAR":
                    fim=input('Escolha inválida! "CONTINUAR" ou "JOGAR".\n')
                if fim == "JOGAR":
                    aposta=False
        elif a == 'T':
            bet = int(input('Quanto quer apostar em Twelve? (30:1)\n'))
            while bet > saldo or bet < 0:
                bet =int(input('Aposte um valor que você CONSIGA apostar! Seu saldo atual: {0}\n'.format(saldo)))
            t += bet
            saldo -= bet
            print('Saldo: {0}'.format(saldo))
            if saldo == 0:
                print('Você não tem mais dinheiro para apostar nessa rodada.')
                input('Aperte ENTER para jogar os dados')
                aposta = False
            else:
                fim = input('Você deseja continuar as apostas ("CONTINUAR") ou rolar os dados ("JOGAR")?\n')
                while fim!="CONTINUAR" and fim!="JOGAR":
                    fim=input('Escolha inválida! "CONTINUAR" ou "JOGAR".\n')
                if fim == "JOGAR":
                    aposta=False
    #registra os tipos de aposta:
    if p>0:
        tipos.append('P')
    if f>0:
        tipos.append('F')
    if c>0:
        tipos.append('C')
    if t>0:
        tipos.append('T')
    #jogando os dados e verificando se ganhou ou não em cada aposta:
    if game:
        #índice da lista tipos:
        x = 0
        n = len(tipos)
        lucro = 0
        dado1 = random.randint(1,6)
        print('Dado 1: {0}'.format(dado1))
        dado2 = random.randint(1,6)
        print('Dado 2: {0}'.format(dado2))
        dados = dado1 + dado2
        print('Soma: {0}'.format(dados))
        while x < n:
            if tipos[x] == 'P':
                if dados== 7 or dados== 11:
                    print('Ganhou em Pass Line!')
                    saldo += 2 * p
                    lucro += p
                elif 2<=dados<=3 or dados==12:
                    print('Perdeu em Pass Line!')
                    lucro -= p
                #passa para a rodada point:
                else:
                    point = True
                    #variável para memorizar o numero tirado em come out para tirar em point:
                    d = dados
            if tipos[x] == 'F':
                if 5 <= dados <= 8:
                    print('Perdeu em Field!')
                    lucro -= p
                elif dados == 2:
                    print('Ganhou o dobro em Field!')
                    saldo += 3 * f
                    lucro += 2 * f
                elif dados == 12:
                    print('Ganhou o triplo em Field!')
                    saldo += 4 * f
                    lucro += 3 * f
                else:
                    print('Ganhou em Field!')
                    saldo += 2 * f
                    lucro += f
            if tipos[x] == 'C':
                if 2<=dados<=3 or dados==12:
                    print('Ganhou em Craps! (x7)')
                    saldo += 8 * c
                    lucro += 7 * c
                else:
                    print('Perdeu em Craps!')
                    lucro -= c
            if tipos[x] == 'T':
                if dados == 12:
                    print('Ganhou em Twelve! (x30)')
                    saldo += 31 * t
                    lucro += 30 * t
                else:
                    print('Perdeu em Twelve!')
                    lucro -= t
            x+=1
        #diferença de dinheiro da rodada
        if lucro < 0:
            print('Seu prejuízo é de {0}.'.format(-lucro))
            if saldo == 0:
                print('Você perdeu, até a próxima!')
                game = False
        elif lucro == 0:
            print('Seu saldo continua igual.')
        else:
            print('Seu lucro é de {0}.'.format(lucro))
    #variável que verifica se já fez aposta em point:
    U = False
    #jogo em point:
    while point:
        aposta2 = True
        if U = True:
            tipos2 = []
        else:
            tipos2 = []
            tipos2.append('P')
        pn = 0
        f = 0
        c = 0
        t = 0
        while aposta2:
            print('Seu saldo atual: {0}'.format(saldo))
            print('Você está na rodada "Point" do jogo!')
            #tipos possíveis de apostas:
            if saldo == 0:
                print('Você não tem nada para apostar!')
                input('Aperte ENTER para jogar os dados')
                aposta2 = False
            else:
                aposta2=True
                a = input('Você gostaria de apostar em: Point ("PN"), Field ("F"), Craps ("C") ou Twelve ("T") ? Por favor escolha um de cada vez!\n(Se você não quiser apostar, digite "NADA")\n'
                '(Caso queria sair do jogo, digite "SAIR")\n')
                if a!= 'PN' and a!='F' and a!='C' and a!='T' and a!="SAIR" and a!="NADA":
                    invalida=True
                    while invalida:
                        a=input('Escolha inválida! Selecione: "PN" para Point, "F" para Field , "C" para Craps ou "T" para Twelve. Caso queira sair escreva "SAIR" ou se você não quiser apostar, digite "NADA" : ')
                        if a=='PN' or a=='F' or a=='C' or a=='T' or a=="SAIR":
                            invalida=False
                        else:
                            invalida=True
                if a == "SAIR":
                    aposta2 = False
                    point = False
                    game = False
                    print('Até mais!')
                elif a == "NADA":
                    input('Aperte ENTER para jogar os dados')
                    aposta2 = False
                #codicionamentos de cada escolha de aposta:
                elif a == 'PN':
                    U = True
                    tipos2 = []
                    #aposta atual:
                    bet = int(input('Quanto quer apostar em Point? (1:1)\n'))
                    while bet > saldo or bet < 0:
                        bet =int(input('Aposte um valor que você CONSIGA apostar! Seu saldo atual: {0}\n'.format(saldo)))
                    pn += bet
                    saldo -= bet
                    print('Saldo: {0}'.format(saldo))
                    if saldo == 0:
                        print('Você não tem mais dinheiro para apostar nessa rodada.')
                        input('Aperte ENTER para jogar os dados')
                        aposta2 = False
                    else:
                        fim = input('Você deseja continuar as apostas ("CONTINUAR") ou rolar os dados ("JOGAR")?\n')
                        while fim!="CONTINUAR" and fim!="JOGAR":
                            fim=input('Escolha inválida! "CONTINUAR" ou "JOGAR".\n')
                        if fim == "JOGAR":
                            aposta2=False
                elif a == 'F':
                    bet = int(input('Quanto quer apostar em Field? (1:1) ou (2:1, se somar 2) ou (3:1, se somar 12)\n'))
                    while bet > saldo or bet < 0:
                        bet =int(input('Aposte um valor que você CONSIGA apostar! Seu saldo atual: {0}\n'.format(saldo)))
                    f += bet
                    saldo -= bet
                    print('Saldo: {0}'.format(saldo))
                    if saldo == 0:
                        print('Você não tem mais dinheiro para apostar nessa rodada.')
                        input('Aperte ENTER para jogar os dados')
                        aposta2 = False
                    else:
                        fim = input('Você deseja continuar as apostas ("CONTINUAR") ou rolar os dados ("JOGAR")?\n')
                        while fim!="CONTINUAR" and fim!="JOGAR":
                            fim=input('Escolha inválida! "CONTINUAR" ou "JOGAR".\n')
                        if fim == "JOGAR":
                            aposta2=False
                elif a == 'C':
                    bet = int(input('Quanto quer apostar em Craps? (7:1)\n'))
                    while bet > saldo or bet < 0:
                        bet =int(input('Aposte um valor que você CONSIGA apostar! Seu saldo atual: {0}\n'.format(saldo)))
                    c += bet
                    saldo -= bet
                    print('Saldo: {0}'.format(saldo))
                    if saldo == 0:
                        print('Você não tem mais dinheiro para apostar nessa rodada.')
                        input('Aperte ENTER para jogar os dados')
                        aposta2 = False
                    else:
                        fim = input('Você deseja continuar as apostas ("CONTINUAR") ou rolar os dados ("JOGAR")?\n')
                        while fim!="CONTINUAR" and fim!="JOGAR":
                            fim=input('Escolha inválida! "CONTINUAR" ou "JOGAR".\n')
                        if fim == "JOGAR":
                            aposta2=False
                elif a == 'T':
                    bet = int(input('Quanto quer apostar em Twelve? (30:1)\n'))
                    while bet > saldo or bet < 0:
                        bet =int(input('Aposte um valor que você CONSIGA apostar! Seu saldo atual: {0}\n'.format(saldo)))
                    t += bet
                    saldo -= bet
                    print('Saldo: {0}'.format(saldo))
                    if saldo == 0:
                        print('Você não tem mais dinheiro para apostar nessa rodada.')
                        input('Aperte ENTER para jogar os dados')
                        aposta2 = False
                    else:
                        fim = input('Você deseja continuar as apostas ("CONTINUAR") ou rolar os dados ("JOGAR")?\n')
                        while fim!="CONTINUAR" and fim!="JOGAR":
                            fim=input('Escolha inválida! "CONTINUAR" ou "JOGAR".\n')
                        if fim == "JOGAR":
                            aposta2=False
        if pn>0:
            tipos2.append('PN')
        if f>0:
            tipos2.append('F')
        if c>0:
            tipos2.append('C')
        if t>0:
            tipos2.append('T')
        #jogando os dados e verificando se ganhou ou não em cada aposta
        if game:
            #índice da lista tipos2
            x = 0
            n = len(tipos2)
            lucro = 0
            dado1 = random.randint(1,6)
            print('Dado 1: {0}'.format(dado1))
            dado2 = random.randint(1,6)
            print('Dado 2: {0}'.format(dado2))
            dados = dado1 + dado2
            print('Soma: {0}'.format(dados))
            while x < n:
                if tipos2[0] == 'P':
                    if dados == d:
                        print('Ganhou em Point!')
                        saldo += 2 * p
                        lucro += p
                        point = False
                    elif dados == 7:
                        print('Perdeu em Point!')
                        lucro -= p
                        point = False
                if tipos2[x]=='PN':
                    if dados == d:
                        print('Ganhou em Point!')
                        saldo += 2 * (pn+p)
                        lucro += (pn+p)
                        point = False
                    elif dados == 7:
                        print('Perdeu em Point!')
                        lucro = lucro-(pn+p)
                        point = False
                if tipos2[x] == 'F':
                    if 5 <= dados <= 8:
                        print('Perdeu em Field!')
                        lucro -= f
                    elif dados == 2:
                        print('Ganhou o dobro em Field!')
                        saldo += 3 * f
                        lucro += 2 * f
                    elif dados == 12:
                        print('Ganhou o triplo em Field!')
                        saldo += 4 * f
                        lucro += 3 * f
                    else:
                        print('Ganhou em Field!')
                        saldo += 2 * f
                        lucro += f
                if tipos2[x] == 'C':
                    if 2<=dados<=3 or dados==12:
                        print('Ganhou em Craps! (x7)')
                        saldo += 8 * c
                        lucro += 7 * c
                    else:
                        print('Perdeu em Craps!')
                        lucro -= c
                if tipos2[x] == 'T':
                    if dados == 12:
                        print('Ganhou em Twelve! (x30)')
                        saldo += 31 * t
                        lucro += 30 * t
                    else:
                        print('Perdeu em Twelve!')
                        lucro -= t
                x += 1
            #diferença de dinheiro da rodada
            if lucro < 0:
                print('Seu prejuízo é de {0}.'.format(-lucro))
                if saldo == 0:
                    print('Você perdeu, até a proxima')
                    game = False
                else:
                    game = True
            elif lucro == 0:
                print('Seu saldo continua igual.')
            else:
                print('Seu lucro é de {0}.'.format(lucro))