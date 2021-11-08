nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

#Calcular média

mediafinal = (nota1 + nota2) / 2

#Verificação
if mediafinal >= 7:
    print('Aprovado: ',mediafinal)
else:
    print('Reprovado: ',mediafinal)

print('=================================================================')

idade = int(input('Digite a sua idade: '))

if idade > 18:
    print('Adulto')
elif idade <18 and idade >12:
    print('Jovem')
else:
    print('Criança')