'''
Faça um programa, que contenha subprogramas, que leia da entrada padrão nomes completos, compostos de nome e sobrenome(s),
de pessoas até que uma string vazia seja lida.
Escreva na saída padrão todos os nomes e sobrenomes com mais de dois caracteres que ocorreram mais que uma vez.
Mostre-os ordenados alfabeticamente. Neste caso implemente subprograma contendo um dos métodos de ordenação visto nas aulas gravadas.
'''

def nomes_digitados(lista): # Separa os nomes
    lista_geral = []
    for i in range(len(lista) - 1):
        valor = lista[i].split()
        lista_geral += valor

    return lista_geral


def remove_repetidos(nomes): # Remove os nomes repetidos mais de uma vez na lista
    repetidos = []
    for i in nomes:
        if i not in repetidos:
            repetidos.append(i)
    repetidos.sort()

    return repetidos

def remove_2caracteres(strings): # Função para remover items com 2 caracteres

    nova_string = []
    for x in range(len(strings)):
        if len(strings[x]) <= 2:
            pass
        else:
            nova_string.append(strings[x])

    return nova_string


# Programa Principal
lista = []
nomes = []

nome_completo = str(input()) # primeira entrada
lista.append(nome_completo)

while nome_completo != '': # Entrada de nomes completos
    nome_completo = str(input())
    lista.append(nome_completo)

nomes_separados = nomes_digitados(lista) # Cria um vetor com nomes separados
nomes_separados = remove_2caracteres(nomes_separados) # Remove strings com menos ou 2 caracteres

for i in range(len(nomes_separados)): # Detecta os Nomes repetidos
    recorrente = nomes_separados.count(nomes_separados[i])
    if recorrente > 1:
        nomes.append(nomes_separados[i])

nomes_repetidos = remove_repetidos(nomes)

for j in range(len(nomes_repetidos)): # Imprime os repetidos
    print(nomes_repetidos[j])
