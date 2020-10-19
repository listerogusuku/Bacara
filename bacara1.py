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
