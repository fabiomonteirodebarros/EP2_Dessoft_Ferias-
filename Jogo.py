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

nome = input('Digite o seu nome: ')

print ('Ok, {}'.format(nome))
print('Segue abaixo um manual de regras:')
print(bcolors.amarelo + '-----------------------------------------------------------------------------------------------' + bcolors.reset)
print(bcolors.amarelo +'|'+ bcolors.reset +'     Você tem direito de realizar 3 pulos                                                    '+ bcolors.amarelo +'|')
print(bcolors.amarelo +'|'+ bcolors.reset +'     Você tem direito de pedir 2 ajudas                                                      '+ bcolors.amarelo +'|')
print(bcolors.amarelo +'|'+ bcolors.reset +'    As dificuldades das perguntas vão aumentando conforme o jogador acerta as respostas      '+ bcolors.amarelo +'|')
print(bcolors.amarelo +'|'+ bcolors.reset +'     Os comandos possiveis são: A - B - C - D - ajuda - pula - parar                         '+ bcolors.amarelo +'|')
print(bcolors.amarelo +'|'+ bcolors.reset +'                                                                                             '+ bcolors.amarelo +'|')
print(bcolors.amarelo +'-----------------------------------------------------------------------------------------------'+ bcolors.reset)
print('BOM JOGO!')


print('O jogo já vai começar!')
sim= input('Digite "sim" se deseja começar o jogo ')
jogo= True
acerto=0
indice = 1
i = 0
pulo= 3
ajuda =2
ja_sorteada = []
lista_comandos = ['A', 'B', 'C', 'D', 'ajuda', 'pula', 'parar']

if sim == 'sim':

    pergunta = sorteia_questao_inedida(transforma, 'facil', ja_sorteada)

    while jogo:
        
        if acerto <= 3:
            nivel = 'facil'
        elif acerto <= 6:
            nivel = 'medio'
        else:
            nivel = 'dificil'

        questao = questao_para_texto(pergunta, indice)
        print(questao)
        resposta= input('\nDigite a alternativa correta: ')

        if resposta == pergunta['correta']:
            acerto += 1
            indice += 1
            print(bcolors.verde + 'Acertou! Seu prêmio atual é R$ {:.2f}\n\n\n'.format(lista_de_valores[i]) + bcolors.reset)
            i += 1
            pergunta = sorteia_questao_inedida(transforma, nivel, ja_sorteada)

        elif resposta== 'pula':
            pulo -= 1
            print('Você utilizou um de seus pulos')
            acerto += 1
            indice += 1
            i += 1
            pergunta = sorteia_questao_inedida(transforma, nivel, ja_sorteada)

        elif resposta == 'ajuda':
            ajuda-=1
            help = gera_ajuda(pergunta)
            print(help)
            print('Número de ajudas disponíveis: {}'.format(ajuda))
            resposta= input('\nDigite a alternativa correta: ')
        
        elif resposta not in lista_comandos:
            print('Essa opção é inválida!')
            print('Os comandos possiveis são: A - B - C - D - ajuda - pula - parar')
            resposta= input('\nDigite a alternativa correta: ')

        elif resposta == 'sair':
            jogo = False
            print('\nQue pena! Você saiu com R${:.2f}'.format(lista_de_valores[i]))

        else:
            jogo = False
            print('O jogo acabou para você, espero que tenha aproveitado!')


        

        


        
        
