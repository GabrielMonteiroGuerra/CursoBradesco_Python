A = input('Informe um valor para a variável A: ')
B = input('Informe um valor para a variável B: ')

if (A > B):
    aux = A
    A = B
    B = aux
print("O Valor da variável A agora é: ",A)
print('O Valor da variável B agora é: ',B)

print('------------------------------------------------------------')

idade = int(input('Digite a sua idade: '))

if idade > 18:
    print('Maior de idade')
else:
    print('Menor de idade')