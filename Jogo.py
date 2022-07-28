from funcoes import *
from questoes import *
from valor import *
import random

problema=valida_questoes(dic)
if len(problema)!= problema.count({}):
    print('A base está errada')
    quit()

transforma= transforma_base(dic)



nome = input('Digite o seu nome: ')

print ('Ok, {0}'.format(nome))
print('Segue abaixo um manual de regras:')
print('- Você tem direito de realizar 3 pulos')
print('- Você tem direito de pedir 2 ajudas')
print('- As dificuldades das perguntas vão aumentando conforme o jogador acerta as respostas')
print('- Os comandos possiveis são: A - B - C - D - ajuda - pula - parar')
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
            print('Você está com R${}'.format(lista_de_valores[i]))
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


        

        


        
        
