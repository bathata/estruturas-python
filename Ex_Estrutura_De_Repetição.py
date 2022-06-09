print('Exercício 1 Estrutura de Repetição\n')
s = 0
for x in range(3,334,3):
  s += x
print('soma =',s)

#=-=-=-=-=-

print('\nExercício 2 Estrutura de Repetição\n')
s = 0
for contador in range(1,11):
  nota = float(input('Digite a nota '+str(contador)+': '))
  s += nota
print('Média = ', s/10)

#=-=-=-=-=-

print('\nExercício 3 Estrutura de Repetição\n')
numero = int(input('Digite o número para a tabuada: '))
for sequencia in range(1,11):
   print('%2d x %2d = %5d' %(sequencia, numero, sequencia*numero))