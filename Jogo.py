from Funcoes import *
from Questoes import *
dic_vazio=[]
problema=valida_questoes(dic)
if len(problema)!= problema.count(dic_vazio):
    print('A base está errada')
    quit()

transforma= transforma_base(dic)



nome = input('Digite o seu nome: ')

print ('Ok, {0}'.format(nome))
print('Segue abaixo um manual de regras:')
print('- Você tem direito de realizar 3 pulos')
print('- Você tem direito de pedir 2 ajudas')
print('- As dificuldades das perguntas vão aumentando conforme o jogador acerta as respostas')
print('- Os comandos possiveis são:\n- "A"\n-"B"\n-"C"\n-"D"\n-"ajuda"\n-"pula"\n-"parar"')
print('BOM JOGO!')


print('O jogo já vai começar!')
sim= input('Digite "sim" se deseja começar o jogo')
acerto= True

if sim == 'sim':
    while acerto:
       i+=1


