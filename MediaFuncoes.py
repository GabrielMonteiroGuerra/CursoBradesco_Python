def lernotas(): #Função para receber a nota
    nota = float(input('Digite uma nota para o aluno(a): '))
    return nota

def resultado(nota1,nota2): #Função para calcular a nota
    media = (nota1 + nota2) / 2
    print('Nota 1: ',nota1)
    print('Nota 2: ',nota2)
    print('Média: ',media," - ", "Resultado: ",end = '')
    if media >= 7:
       print('Aprovado!')
    else:
       print('Reprovado!')

a = lernotas()
b = lernotas()
resultado(a,b)