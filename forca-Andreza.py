import random #importa a biblioteca random 

palavras = []#as palavras que estão entre os colchetes formam uma lista
letrasErradas = ''
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def inserir(): #inserir as palavras que desejar 
    while True:
        x= input("Digite a palavra: ")
        palavras.append(x)
        if x == '': #se apertar enter e estiver vazio o jogo começa
            break
def principal(): #o def serve para definir uma função
    """
    Função Princial do programa
    """
    print('F O R C A')
    inserir ()

    palavraSecreta = sortearPalavra()
    palpite = ''
    desenhaJogo(palavraSecreta,palpite)

    while True: #while True repete infinitamente um bloco de instrução enquanto sua condição é verdadeira'''
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo(): #if significa Se, o comando só será executado se a condição for verdadeira'''
            print('Voce Perdeu!!!')
            break #O break serve para finalizar a repetição da instrução'''
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
        
def perdeuJogo():
    global FORCAIMG #Significa que o comando não é local,ou seja, ele funcionará em qualquer parte do código
    if len(letrasErradas) == len(FORCAIMG): #o len retorna o tamanho da lista
        return True #O return true termina a execução da função, retornando o resultado (opcional) e o controle para a rotina que a chamou.
    else:
        return False # 
    
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True
    for letra in palavraSecreta: #for in é o código que será repetido
        if letra not in letrasCertas: #O operador in verifica se o operando a sua esquerda, está contido na lista a sua direita, da mesma forma
                                         #que o operador not in que verifica o contrário.

            ganhou = False #False=falso
    return ganhou  #return=retornar     
        


def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ") #input serve para receber dados fornecidos pelo usuário
    palpite = palpite.upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas: #or=ou
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z": #O modificador not é uma palavrinha que serve pra negar a expressão do if ou elif,nesse caso, o elif.
        print('Por favor escolha apenas letras')
    else:
        return palpite
    
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()

    
principal()
