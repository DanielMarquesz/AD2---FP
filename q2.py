## funcao para retornar lista de numeros perfeitos
def calcula_perfeitos(lista):
    perf = list()

    for numero in lista:
        soma_div = 0
        for divisor in range(1, numero - 1):
            if numero % divisor == 0:
                soma_div += divisor
            if soma_div > numero:
                break
        if soma_div == numero:
            perf.append(numero)

    return perf


## funca pra imprimir lista de perfeitos
def imprime(lista):
    print('Relação de Números Perfeitos:')
    for numero in lista:
        print(numero)
    print('Fim da Relação')

## input para as entradas
numeros = input()

## passando para lista para separar os numeros
numeros_lista = numeros.split()

## verificando se nao foi passada uma string vazia
if numeros_lista[0] != '':
    ## passando os numeros para o tipo inteiro
    for indice, numero in enumerate(numeros_lista):
        numeros_lista[indice] = int(numero)

    perfeitos = calcula_perfeitos(numeros_lista)
    imprime(perfeitos)

else:
    print('Nenhum Número Foi Lido!!!')

