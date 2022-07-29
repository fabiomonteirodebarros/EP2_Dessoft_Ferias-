# Função Transforma Base de Questões :
def transforma_base(lista):
    dic={}
    for indice in lista:
        if indice['nivel'] not in dic.keys():
            dic[indice['nivel']]=[]
        dic[indice['nivel']].append(indice)  
    return dic

# Função Valida uma Questão:
def valida_questao(dic):
    lista=['A', 'B', 'C', 'D']
    dic_final={}
    dic_aux={}
    for chave in ['titulo', 'nivel', 'opcoes', 'correta']:
        if chave not in dic.keys():
            dic_final[chave]='nao_encontrado'
               
    if len(dic.keys()) != 4:
        dic_final['outro']= 'numero_chaves_invalido'
    
    if 'titulo' in dic.keys() and len(dic['titulo'].strip())==0:
        dic_final['titulo']= 'vazio'
    
    if 'nivel' in dic.keys():
        if dic['nivel'] not in ['facil', 'medio', 'dificil']:
            dic_final['nivel']= 'valor_errado'
        
    if 'opcoes' in dic.keys():
        if len(dic['opcoes']) !=4:
            dic_final['opcoes']= 'tamanho_invalido'
        else:
            for opcoes,resposta in dic['opcoes'].items():
                if opcoes not in ['A', 'B', 'C', 'D']:
                    dic_final['opcoes']= 'chave_invalida_ou_nao_encontrada'
                else:
                    if len(str(resposta).strip())==0:
                        dic_aux[opcoes]= 'vazia'
            if len(dic_aux)>0:
                dic_final['opcoes']=dic_aux
    if 'correta' in dic.keys():
        if dic['correta'] not in ['A', 'B', 'C', 'D']:
            dic_final['correta']= 'valor_errado'

    return dic_final

# Função Valida Lista de Questões:
def valida_questoes(lista):
    lista_erros=[]
    i=0
    while i<len(lista):
        validacao=valida_questao(lista[i])
        lista_erros.append(validacao)
        i+=1
    return lista_erros

#Função Sorteia uma Questão:
import random

def sorteia_questao(dic, string):
    dic_final={}
    for nivel,questao in dic.items():
        if nivel == string:
            dic_final=questao
    questao= random.choice(dic_final)
    return questao

#Função Sorteia uma Questão Inédita:
def sorteia_questao_inedida(dic, string, lista):
    retorno=True
    while retorno:
        sorteio= random.choice(dic[string])
        if sorteio not in lista:
            lista.append(sorteio)
            retorno = False
    return sorteio

#Função Questão para Texto:
def questao_para_texto(dic, indice):
    questao_escrita = '----------------------------------------'
    questao_escrita+= '\n''QUESTAO ' +str(indice)+'\n'+'\n'
    questao_escrita+= dic['titulo']
    questao_escrita+= '\n'+'\n''RESPOSTAS:''\n'
    for alg,alternativa in dic['opcoes'].items():
        questao_escrita+= alg + ': '+alternativa+'\n'
    return questao_escrita

#Função Gera Ajuda em uma Questão:
import random

def gera_ajuda(questao):
    lista_pode=[]
    for perg,alt in questao['opcoes'].items():
        if perg != questao['correta']:
            lista_pode.append(alt)
    
    num = random.randint(1,2)
    tip = random.sample(lista_pode, k=num)

    texto1= 'DICA:\n'
    texto1 += 'Opçoes certamente erradas: ' + ' |'.join(tip)
    return texto1