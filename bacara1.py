# EP | Exercício Programa: Bacará Simplificado | Design de Software
# Equipe: Celina Vieira de Melo e Lister Ogusuku Ribeiro
# Data: 18/10/2020

#Descrição:
#Jogo de bacará criado com a intenção de promover uma interatividade com o usuário,
#onde este aposta em quem será o vencedor da partida (jogador, banco ou empate) e, por fim, todo
#o restante do jogo é realizado pela mesa de acordo com as regras simplificadas definidas ao longo
#do programa pelo programador.

#Neste jogo foram implementadas todas as regras avançadas.

#============================

#Importação da biblioteca "Random", que ajudará meu código a gerar números aleatórios

import random

#Iniciando o jogo e entregando a quantidade n de fichas definida pelo programador.

print("Começo do jogo \nVocê recebeu 100 fichas! ") #Programa diz ao jogador que o jogo começou e que ele recebeu 100 fichas.
soma=100
aux=0
while aux==0:
    while soma>0:
        Aposta=input("Em quem você quer apostar? ")               # "Aposta" recebe a aposta do usuário do jogo.
        while Aposta != 'Jogador' and Aposta!='jogador' and Aposta !='Banco' and Aposta != 'banco' and Aposta!='Empate' and Aposta!='empate':
            print("Não entendi, em quem você quer apostar? ")     # "Fichas" recebe o valor de fichas que o apostador deseja apostar.
            Aposta=input("Em quem você quer apostar? ")

        Fichas=int(input("Quantas fichas você quer apostar? "))

# Criação de um While para impedir que o usuário adicione mais fichas do que o permitido:

        while Fichas > soma:
            print('Número de fichas maior que o permitido!')
            Fichas = int(input('Digite novo número de fichas: '))

        numero_de_baralhos=int(input("Quantos baralhos você quer? 1, 6 ou 8: "))

# Criação de um While para impedir que o usuário adicione mais baralhos do que o permitido:

        while numero_de_baralhos != 1 and numero_de_baralhos != 6 and numero_de_baralhos != 8:
            print('Número de baralhos não permitido!')
            numero_de_baralhos=int(input("Quantos baralhos você quer? 1, 6 ou 8: ")) 

        baralho=[0,'Ás', 2, 3, 4, 5, 6, 7, 8, 9, 10,'K', 'Q', 'J']  # Criação de uma lista com os índices do baralho.
        naipe=['Ouro','Paus','Copas','Espada'] 

        num_cartas = []
        i = 0
        while i <= 13:  #Atribui a quantidade de cartas que tem em cada naipe dependendo do numero de baralhos.
            num_cartas.append([numero_de_baralhos,numero_de_baralhos,numero_de_baralhos,numero_de_baralhos])
            i += 1
        print('Seu baralho possui', numero_de_baralhos*(len(baralho)-1)*4, 'cartas') 


        # Sorteia uma carta e um naipe por meio da biblioteca random:

        carta1_Jogador=random.randint(1,13)
        naipe1_Jogador=random.randint(0,3)
        c1j=baralho[carta1_Jogador]
        n1j=naipe[naipe1_Jogador]

        # While que atribui às cartas maiores que 9 o valor 0 e mostra ao usuário qual carta ele tirou:

        while num_cartas[carta1_Jogador][naipe1_Jogador]==0:
            carta1_Jogador=random.randint(1,13)
            naipe1_Jogador=random.randint(0,3)
            c1j=baralho[carta1_Jogador]
            n1j=naipe[naipe1_Jogador]
        num_cartas[carta1_Jogador][naipe1_Jogador]-=1

        if baralho[carta1_Jogador]==10 or baralho[carta1_Jogador]=='K' or baralho[carta1_Jogador]=='Q' or baralho[carta1_Jogador]=='J':
            carta1_Jogador=0
        print("A primeira carta do jogador é {} de {}, que equivale a {} ".format(c1j,n1j,carta1_Jogador))

        # Sorteia uma carta e um naipe por meio da biblioteca random:

        carta2_Jogador=random.randint(1,13)
        naipe2_Jogador=random.randint(0,3)
        c2j=baralho[carta2_Jogador]
        n2j=naipe[naipe1_Jogador]

        # While que atribui às cartas maiores que 9 o valor 0 e mostra ao usuário qual carta ele tirou:

        while num_cartas[carta2_Jogador][naipe2_Jogador]==0:
            carta2_Jogador=random.randint(1,13)
            naipe2_Jogador=random.randint(0,3)
            c2j=baralho[carta2_Jogador]
            n2j=naipe[naipe2_Jogador]
        num_cartas[carta2_Jogador][naipe2_Jogador]-=1
        if baralho[carta2_Jogador]==10 or baralho[carta2_Jogador]=='K' or baralho[carta2_Jogador]=='Q' or baralho[carta2_Jogador]=='J':
            carta2_Jogador=0
        print("A segunda carta do jogador é {} de {}, que equivale a {}".format(c2j,n2j,carta2_Jogador))

        # Mostra a soma das cartas do jogador:

        soma_jogador=(carta1_Jogador+carta2_Jogador)%10
        print('A soma das cartas do jogador é {} '.format(soma_jogador))

        # Sorteia uma carta e um naipe por meio da biblioteca random:

        carta1_Banco=random.randint(1,13)
        naipe1_Banco=random.randint(0,3)
        c1b=baralho[carta1_Banco]
        n1b=naipe[naipe1_Banco]

        # While que atribui às cartas maiores que 9 o valor 0 e mostra ao usuário qual carta ele tirou:

        while num_cartas[carta1_Banco][naipe1_Banco]==0:
            carta1_Banco=random.randint(1,13)
            naipe1_Banco=random.randint(0,3)
            c1b=baralho[carta1_Banco]
            n1b=naipe[naipe1_Banco]
        num_cartas[carta1_Banco][naipe1_Banco]-=1
        if baralho[carta1_Banco]==10 or baralho[carta1_Banco]=='K' or baralho[carta1_Banco]=='Q' or baralho[carta1_Banco]=='J':
            carta1_Banco=0
        print("A primeira carta do banco é {} de {}, que equivale a {}".format(c1b,n1b, carta1_Banco))

        # Sorteia uma carta e um naipe por meio da biblioteca random:

        carta2_Banco=random.randint(1,13)
        naipe2_Banco=random.randint(0,3)
        c2b=baralho[carta2_Banco]
        n2b=naipe[naipe2_Banco]

        # While que atribui às cartas maiores que 9 o valor 0 e mostra ao usuário qual carta ele tirou:

        while num_cartas[carta2_Banco][naipe2_Banco]==0:

            carta2_Banco=random.randint(1,13)
            naipe2_Banco=random.randint(0,3)
            c2b=baralho[carta2_Banco]
            n2b=naipe[naipe2_Banco]

        num_cartas[carta2_Banco][naipe2_Banco]-=1
        if baralho[carta2_Banco]==10 or baralho[carta2_Banco]=='K' or baralho[carta2_Banco]=='Q' or baralho[carta2_Banco]=='J':
            carta2_Banco=0
        print("A segunda carta do banco é {} de {}, que equivale a {} ".format(c2b,n2b,carta2_Banco))

        # Mostra a soma das cartas do banco:

        soma_banco=(carta1_Banco+carta2_Banco)%10
        print('A soma das cartas do banco é {}'.format(soma_banco))

        # Regras para a carta puxada do jogador:

        jogador_puxou=0
        if soma_jogador<=5:
            jogador_puxou=1
            print("Jogador puxa outra carta!")   

            # Sorteia carta 3 do jogador:

            carta3_Jogador=random.randint(1,13)
            naipe3_Jogador=random.randint(0,3)
            c3j=baralho[carta3_Jogador]
            n3j=naipe[naipe3_Jogador]

            # While que atribui às cartas maiores que 9 o valor 0 e mostra ao usuário qual carta ele tirou:

            while num_cartas[carta3_Jogador][naipe3_Jogador]==0:
                carta3_Jogador=random.randint(1,13)
                naipe3_Jogador=random.randint(0,3)
                c3j=baralho[carta3_Jogador]
                n3j=naipe[naipe3_Jogador]
            num_cartas[carta3_Jogador][naipe3_Jogador]-=1

            if baralho[carta3_Jogador]==10 or baralho[carta3_Jogador]=='K' or baralho[carta3_Jogador]=='Q' or baralho[carta3_Jogador]=='J':
                carta3_Jogador=0
            print("A terceira carta do jogador é {} de {}, que equivale a {} ".format(c3j,n3j,carta3_Jogador))
            print("A nova soma do jogador é {}".format((soma_jogador+carta3_Jogador)%10))

        # Regras avançadas para receber a 3ª carta:

        if soma_banco<=5 and jogador_puxou==0:
            print ("Banco puxa outra carta")
            carta3_Banco=random.randint(1,13)
            naipe3_Banco=random.randint(0,3)
            c3b=baralho[carta3_Banco]
            n3b=naipe[naipe3_Banco]
            while num_cartas[carta3_Banco][naipe3_Banco]==0:
                carta3_Banco=random.randint(1,13)
                naipe3_Banco=random.randint(0,3)
                c3b=baralho[carta3_Banco]
                n3b=naipe[naipe3_Banco]
            num_cartas[carta3_Banco][naipe3_Banco]-=1
            if baralho[carta3_Banco]==10 or baralho[carta3_Banco]=='K' or baralho[carta3_Banco]=='Q' or baralho[carta3_Banco]=='J':
                carta3_Banco=0
            print("A terceira carta do banco é {} de {}, que equivale a {}".format(c3b,n3b,carta3_Banco))
            print("A nova soma do banco é {}".format((soma_banco+carta3_Banco)%10))

        if soma_banco<=5 and jogador_puxou==1:  
            if soma_banco<=3 and soma_jogador !=8:
                print("Banco puxa outra carta!")
            carta3_Banco=random.randint(1,13)
            naipe3_Banco=random.randint(0,3)
            c3b=baralho[carta3_Banco]
            n3b=naipe[naipe3_Banco]

            # Criação de um While para impedir que o usuário adicione mais fichas do que o permitido:

            while num_cartas[carta3_Banco][naipe3_Banco]==0:
                carta3_Banco=random.randint(1,13)
                naipe3_Banco=random.randint(0,3)
                c3b=baralho[carta3_Banco]
                n3b=naipe[naipe3_Banco]
            num_cartas[carta3_Banco][naipe3_Banco]-=1
            if baralho[carta3_Banco]==10 or baralho[carta3_Banco]=='K' or baralho[carta3_Banco]=='Q' or baralho[carta3_Banco]=='J':
                carta3_Banco=0
            print("A terceira carta do banco é {} de {}, que equivale a {}".format(c3b,n3b,carta3_Banco))
            print("A nova soma do banco é {}".format((soma_banco+carta3_Banco)%10))
            if soma_banco==4 and carta3_Jogador>1 and carta3_Jogador<8:  # Adição de mais uma exceção para puxar a 3ª carta.
                print("Banco puxa outra carta!")
            
            if soma_banco==5 and carta3_Jogador>3 and carta3_Jogador<8:  # Adição de mais uma exceção para puxar a 3ª carta.
                print("Banco puxa outra carta!")
            
            
        # "ifs" e "elifs" que dizem se o jogador ou o banco ganhou; se sua aposta foi em quem ganhou e a distribuição dos pontos para a casa e para o usuário.

        if soma_jogador>soma_banco:
            print("Jogador ganhou!")   
            if Aposta=="Jogador" or Aposta=="jogador":
                print("Você ganhou e recebe {0} fichas. Sua nova soma é {1} ".format(Fichas, soma+Fichas))
                soma+=Fichas
                if numero_de_baralhos==1:  #se jogador ganhar
                    print("Você pagará para casa {} fichas. Sua nova soma é {} ".format(int(0.0129*Fichas), soma-int(0.0129*Fichas)))
                    soma+=Fichas-int(0.0129*Fichas)
                elif numero_de_baralhos==6:
                    print("Você pagará para casa {} fichas. Sua nova soma é {} ".format(int(0.0124*Fichas), soma-int((0.0124*Fichas))))
                    soma+=Fichas-int((0.0124*Fichas))
                else:
                    print("Você pagará para casa {} fichas. Sua nova soma é {} ".format(int(0.0124*Fichas), soma-int((0.0124*Fichas))))
                    soma+=Fichas-int((0.0124*Fichas))
            else:
                print("Você perdeu {0} fichas. Sua nova soma é {1}\nNão pague nada a casa ".format(Fichas, soma-Fichas))
                soma=soma-Fichas

        elif soma_banco>soma_jogador:
            print("Banco ganhou!")
            if Aposta=="Banco" or Aposta=="banco":
                print("Você ganhou e recebe {0} fichas. Sua nova soma é {1} ".format(int(0.95*Fichas),soma+int(0.95*Fichas)))
                soma=soma+int(0.95*Fichas)
                if numero_de_baralhos==1:  #se empate
                    print("Você pagará para casa {} fichas. Sua nova soma é {} ".format(int(0.1575*Fichas), soma-int((0.1575*Fichas))))
                    soma=soma+Fichas-int((0.1575*Fichas))
                elif numero_de_baralhos==6:
                    print("Você pagará para casa {} fichas. Sua nova soma é {} ".format(int(0.1444*Fichas), soma-int((0.1444*Fichas))))
                    soma=soma+Fichas-int((0.1444*Fichas))
                else:
                    print("Você pagará para casa {} fichas. Sua nova soma é {} ".format(int(0.1436*Fichas), soma-int((0.1436*Fichas))))
                    soma=soma+Fichas-int((0.1436*Fichas))
            else:
                print("Você perdeu {0} fichas. Sua nova soma é {1}\nNão pague nada a casa ".format(Fichas, soma-Fichas))
                soma=soma-Fichas        
               
