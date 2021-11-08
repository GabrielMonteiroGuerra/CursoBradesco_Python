#Dividir a programação em blocos para facilitar o entendimento e a manutenção do software
#Nome, parâmetros e corpo

#def - início da função
#Parâmetros - Dados que a função vai receber para o processamento
#Corpo - Local onde será feito o processamentos dos dados
#return - quando tiver a necessidade de retornar um dado
#Tem que ter indentação

def mensagem1():
    print('Hello World!')

def mensagem2():
    return 'Hello World'

mensagem1()

texto = mensagem2()

print(texto)