'''
Desenvolva os exercícios a seguir utilizando o conceito de listas, tuplas, sets ou dicionários:

Crie uma list de int vetB com tamanho 5, insira um inteiro com entrada do teclado para cada um dos elementos e mostre
na tela os seus valores após a inserção dos elementos.

Crie uma list de int vetD com tamanho 50, atribua ao conteúdo de cada um de seus elementos o valor de seu índice e
mostre o valor de cada um dos elementos na tela multiplicados por 2.

Crie uma tupla contendo todos os meses do ano e mostre qual mês corresponde ao índice 8.

Crie um set contendo as partes de um computador e depois adicione o item “memória RAM” e mostre o set na tela.

Crie um dicionário que guarde as informações de 5 conceitos de Python que você aprendeu até agora.

'''

vetB = [int]*5
for i in range(len(vetB)):
    while True:
        try:
            v = int(input('Insira valores inteiros :'))
        except ValueError:
            print('Somente numeros inteiros')
            continue
        else:
            vetB[i] = v
            break
print(vetB)


vetD = [int]*50
for i in range(len(vetD)):
    vetD[i] = i
for n in vetD:
    print(n*2)


meses = ('janeiro','fevereiro','março','abril','maio','junho','julho', 'agosto','setembro','outubro','novembro','dezembro')
print(meses[8])


computador = ('Monitor', 'CPU', 'Placa de video','HD')
computador = set(computador)
computador.add('Memoria ram')
print(computador)


dicionario = {0: 'Bonito é melhor que feio.', 1: 'Explícito é melhor que implícito.',
              2: 'Simples é melhor que complexo.', 3: 'Complexo é melhor que complicado.',
              4: 'Linear é melhor do que aninhado.'}

print(dicionario)
