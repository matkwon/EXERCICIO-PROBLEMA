import random
saldo = 500
game = True
while game:
    aposta = True
    point = False
    #guarda os tipos de apostas:
    tipos = []
    #variáveis que guardam as apostas de cada tipo:
    p = 0
    f = 0
    c = 0
    t = 0
    while aposta:
        #variáveis que identificam se a aposta já foi feita para que, então, não se guarde repetidos na lista de tipos:
        i = 0
        l = 0
        z = 0
        print('Seu saldo atual: {0}'.format(saldo))
        print('Você está na rodada "Come out" do jogo!')
        #tipos possíveis de apostas:
        a = input('Você gostaria de apostar em: Pass Line ("p"), Field ("f"), Craps ("c") ou Twelve ("t")? Por favor escolha um de cada vez!\n'
        '(Caso queria sair do jogo, digite "sair")\n')
        while a != 'p' or 'f' or 'c' or 't' or 'sair':
            a = input('Inválido! Digite alguma das opções: "p", "f", "c", "t" ou "sair"\n')
        if a == "sair":
            aposta = False
            game = False
            print('Até mais!')
        #condicionamentos de cada escolha de aposta:
        elif a == 'p':
            while i < l:
                if tipos[i] != 'p':
                    i += 1
                    z += 1
            if z == l:
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
            while i < l:
                if tipos[i] != 'p':
                    i += 1
                    z += 1
            if z == l:
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
            while i < l:
                if tipos[i] != 'p':
                    i += 1
                    z += 1
            if z == l:
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
            while i < l:
                if tipos[i] != 'p':
                    i += 1
                    z += 1
            if z == l:
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
        l = len(tipos)
    #jogando os dados e verificando se ganhou ou não em cada aposta:
    if game:
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
            if tipos[x] == 'p':
                if dados == 7 or 11:
                    print('Ganhou em Pass Line!')
                    saldo += 2 * p
                    lucro += p
                elif dados == 2 or 3 or 12:
                    print('Perdeu em Pass Line!')
                    lucro -= p
                else:
                    point = True
                    #variável para memorizar o point:
                    d = dados
                x += 1
            if tipos[x] == 'f':
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
                x += 1
            if tipos[x] == 'c':
                if dados == 2 or 3 or 12:
                    print('Ganhou em Craps! (x7)')
                    saldo += 8 * c
                    lucro += 7 * c
                else:
                    print('Perdeu em Craps!')
                    lucro -= c
                x += 1
            if tipos[x] == 't':
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
        elif lucro == 0:
            print('Seu saldo continua igual.')
        else:
            print('seu lucro é de {0}.'.format(lucro))
    #jogo em point:
    while point:
        aposta2 = True
        tipos2 = ['p']
        f = 0
        c = 0
        t = 0
        while aposta2:
            i = 0
            l = 0
            z = 0
            print('Seu saldo atual: {0}'.format(saldo))
            print('Você está na rodada "Point" do jogo!')
            #tipos possíveis de apostas:
            a = input('Você gostaria de apostar em: Point ("p"), Field ("f"), Craps ("c") ou Twelve ("t")? Por favor escolha um de cada vez!\n'
            '(Caso queria sair do jogo, digite "sair")\n')
            while a != 'p' or 'f' or 'c' or 't' or 'sair':
                a = input('Inválido! Digite alguma das opções: "p", "f", "c", "t" ou "sair"\n')
            if a == "sair":
                aposta2 = False
                point = False
                game = False
                print('Até mais!')
            #condicionamentos de cada escolha de aposta:
            elif a == 'p':
                bet = int(input('Quanto quer apostar em Point? (1:1)\n'))
                while bet > saldo or bet < 0:
                    bet = input('Aposte um valor que você CONSIGA apostar! Seu saldo atual: {0}\n'.format(saldo))
                p += bet
                saldo -= bet
                print('Saldo: {0}'.format(saldo))
                fim = input('Você deseja continuar as apostas ("a") ou rolar os dados ("d")?\n')
                while fim != 'a' and 'd':
                    input('Escolha inválida! "a" ou "d".\n')
                if fim == 'd':
                    aposta2 = False
            elif a == 'f':
                while i < l:
                    if tipos[i] != 'p':
                        i += 1
                        z += 1
                if z == l:
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
                    aposta2 = False
            elif a == 'c':
                while i < l:
                    if tipos[i] != 'p':
                        i += 1
                        z += 1
                if z == l:
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
                    aposta2 = False
            elif a == 't':
                while i < l:
                    if tipos[i] != 'p':
                        i += 1
                        z += 1
                if z == l:
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
                    aposta2 = False
            l = len(tipos)
        #jogando os dados e verificando se ganhou ou não em cada aposta
        if game:
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
                if tipos[x] == 'p':
                    if dados == d:
                        print('Ganhou em Point!')
                        saldo += 2 * p
                        lucro += p
                        point = False
                    elif dados == 7:
                        print('Perdeu em Point!')
                        lucro -= p
                        point = False
                    x += 1
                if tipos[x] == 'f':
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
                    x += 1
                if tipos[x] == 'c':
                    if dados == 2 or 3 or 12:
                        print('Ganhou em Craps! (x7)')
                        saldo += 8 * c
                        lucro += 7 * c
                    else:
                        print('Perdeu em Craps!')
                        lucro -= c
                    x += 1
                if tipos[x] == 't':
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
            elif lucro == 0:
                print('Seu saldo continua igual.')
            else:
                print('seu lucro é de {0}.'.format(lucro))