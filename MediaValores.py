quantidade = 0
soma = 0
media = 0
valor = float(input('Digite o valor: '))

while (valor > 0):
    soma = soma + valor
    quantidade = quantidade + 1
    valor = float(input('Digite o valor: '))

media = soma / quantidade
print('Total da soma: ',soma)
print('Quantidade de valores digitados: ',quantidade)
print('Média dos valores: ',media)