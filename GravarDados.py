#Gravando dados em txt

arquivo = open('arqText.txt','w') #W abre o arquivo para escrita

arquivo.write('Curso Python \n') #Escrevendo dados no arquivo txt
arquivo.write('Aula Prática \n') #Escrevendo dados no arquivo txt
arquivo.write('Gabriel Monteiro Guerra - Itaú') #Escrevendo dados no arquivo txt
arquivo.close()

#Leitura de um arquivo texto
leitura = open('arqText.txt','r') #R Abre o arquivo para leitura
print(leitura.read()) #Lendo o conteúdo que foi gravado
leitura.close()

