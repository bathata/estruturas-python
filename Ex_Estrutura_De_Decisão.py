#=-=-=-=-=-

print('Exercício 1 sobre estrutura de decisão\n')

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1+nota2)/2

print('Média = ',media)

if media >= 6:
    print('Você foi aprovado')
  
else:
    print('Você foi reprovado')

print('-'* 35)
print('Exercício 2 sobre estrutura de decisão')

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1+nota2)/2

print('Média = ',media)

if media >= 6:
    print('Você foi aprovado')

elif media >= 4:
    print('Exame!')
  
else:
    print('Você foi reprovado')
