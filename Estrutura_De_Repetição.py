print('Exemplo 1 de While\n')
senha = '11'
leitura = ' '

while (leitura != senha): 
  leitura = input('Digite a senha: ')
  
  if leitura == senha:
      print('Acesso liberado')
  else:
      print('Senha incorreta. Tente novamente')
    
#=-=-=-=-=-

print('\nExemplo 2 de While\n')

contador = 0
somador = 0 

while contador < 5:
  contador = contador + 1 
  valor = float(input('Digite o '+str(contador)+'º valor: '))
  somador = somador + valor
   #não pode ser colocada uma variável inteira dentro do float, por isso ela é colocada(RETORNADA) como string
  #NÃO TEM NADA DE ++ DONA THATA!!!!!!!!!
print('Soma = ',somador)

#=-=-=-=-=-

print('\nExemplo 1 de FOR\n Encontrar a soma S = 1+4+7+10+13+16+19\n')

s = 0

for x in range(1,20,3):
    s += x
print('Soma = ',s)

#=-=-=-=-=-

print('\nExemplo 2 de FOR\nAs notas de um aluno estão armazenadas em uma lista. Calcular a média dessas notas.')

ListaNotas = [3.4, 6.6, 8, 9, 10, 9.5, 8.8, 4.3]
soma = 0
for nota in ListaNotas:
  soma += nota
media = soma/len(ListaNotas)
print('Media = %.2f'%media)