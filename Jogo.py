from cgitb import reset
from funcoes import *
from questoes import *
from valor import *
import random

problema=valida_questoes(dic)
if len(problema)!= problema.count({}):
    print('A base está errada')
    quit()

transforma= transforma_base(dic)

class bcolors:
  cinza = '\033[1;30m'
  roxo = '\033[0;35m'
  vermelho = '\033[0;31m'
  amarelo = '\033[1;33m'
  azul_claro = '\033[1;36m'
  azul = '\033[1;34m'
  reset = '\033[0m'
  verde = '\033[1;32m'
  laranja = '\033[1;32m'

nome = input(bcolors.azul+'Digite o seu nome: ')



print (bcolors.cinza+'Ok, {}'.format(nome))
print(bcolors.cinza+'Segue abaixo um manual de regras:')
print(bcolors.amarelo + '-----------------------------------------------------------------------------------------------' + bcolors.reset)
print(bcolors.amarelo +'|'+ bcolors.cinza +'     Você tem direito de realizar 3 pulos                                                    '+ bcolors.amarelo +'|')
print(bcolors.amarelo +'|'+ bcolors.cinza +'     Você tem direito de pedir 2 ajudas                                                      '+ bcolors.amarelo +'|')
print(bcolors.amarelo +'|'+ bcolors.cinza +'    As dificuldades das perguntas vão aumentando conforme o jogador acerta as respostas      '+ bcolors.amarelo +'|')
print(bcolors.amarelo +'|'+ bcolors.cinza +'     Os comandos possiveis são: A - B - C - D - ajuda - pula - parar                         '+ bcolors.amarelo +'|')
print(bcolors.amarelo +'|'+ bcolors.cinza +'                                                                                             '+ bcolors.amarelo +'|')
print(bcolors.amarelo +'-----------------------------------------------------------------------------------------------'+ bcolors.reset)
print(bcolors.cinza+'BOM JOGO!'+bcolors.reset)
#Aqui são apenas os prints iniciais do jogo

print('O jogo já vai começar!')
sim= input('Digite "sim" se deseja começar o jogo ')
acerto=0
indice = 1
i = 0
pulo= 3
ajuda =2
ja_sorteada = []
lista_comandos = ['A', 'B', 'C', 'D', 'ajuda', 'pula', 'parar']
jogar_novamente='S'
#Acima foram criadas as variáveis que vão auxiliar no andamento do jogo
if sim == 'sim':

    pergunta = sorteia_questao_inedida(transforma, 'facil', ja_sorteada)#Uso da função Sorteia Questão Inédita

    while jogar_novamente:#loop principal do jogo
        
        if acerto <= 3:# Dividimos os niveis das perguntas pela quantidade de acerto
            nivel = 'facil'
        elif acerto <= 6:
            nivel = 'medio'
        else:
            nivel = 'dificil'

        questao = questao_para_texto(pergunta, indice)#Uso da função Sorteia Questão para Texto
        print(questao)
        resposta= input('\nDigite a alternativa correta: ')

        if resposta == pergunta['correta']:
            acerto += 1
            indice += 1
            print(bcolors.verde + 'Acertou! Seu prêmio atual é R$ {:.2f}\n\n\n'.format(lista_de_valores[i]) + bcolors.reset)
            i += 1
            pergunta = sorteia_questao_inedida(transforma, nivel, ja_sorteada)#Uso da função Sorteia Questão Inédita
        #Caso o jogador acerte a questão um valor será somado ao seu saldo e ele irá receber outra pergunta 

        elif resposta== 'pula':
            if pulo <=0:
                print(bcolors.vermelho+'Você já gastou todos os seus pulos'+bcolors.reset)
            else:
                print(bcolors.amarelo+'Você utilizou um de seus pulos. Seu prêmio atual é R$ {:.2f}'.format(lista_de_valores[i])+bcolors.reset)
                print(bcolors.laranja+'Agora restam {} pulo(s)'.format(pulo-1)+bcolors.reset)
                acerto += 1
                indice += 1
                i += 1
                pergunta = sorteia_questao_inedida(transforma, nivel, ja_sorteada)#Uso da função Sorteia Questão Inédita
            pulo -= 1
            #Aqui temos o recurso de pulo

        elif resposta == 'ajuda':
            if ajuda <=0:
                print(bcolors.vermelho+'Você não tem mais ajuda disponível'+bcolors.reset)
            if ajuda>0:
                help = gera_ajuda(pergunta)#Uso da função Gera Ajuda
                print(bcolors.verde+help+bcolors.reset)
                print(bcolors.amarelo+'Número de ajudas disponíveis: {}'.format(ajuda-1)+bcolors.reset)
            ajuda-=1
            #Aqui são as condições caso o jogador peça ajuda
        
        elif resposta not in lista_comandos:
            print(bcolors.vermelho+'Essa opção é inválida!')
            print(bcolors.laranja+'Os comandos possiveis são: A - B - C - D - ajuda - pula - parar'+bcolors.reset)

        elif resposta == 'sair':
            print(bcolors.roxo+'\nQue pena! Você saiu com R${:.2f}'.format(lista_de_valores[i]))
            jogar_novamente=input(bcolors.azul_claro+'Quer jogar novamente[S/N]?'+ bcolors.reset)
            break
            #Caso o jogador queira sair com o dinheiro já acumulado

        else:
            print(bcolors.roxo+'O jogo acabou para você, espero que tenha aproveitado!'+bcolors.reset)
            jogar_novamente=input(bcolors.azul_claro+'Quer jogar novamente[S/N]?'+ bcolors.reset)
            #Caso o jogador perca
            if jogar_novamente == 'N':
                print('Até a próxima!')
                break
            else:
                pergunta = sorteia_questao_inedida(transforma, 'facil', ja_sorteada)#Uso da função Sorteia Questão Inédita
            #Caso o jogador queira jogar mais uma vez


                




        

        


        
        
