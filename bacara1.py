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
        
