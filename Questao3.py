from math import sqrt
'''
Calcular a média do centroíde,

Usar as coordenadas do centroíde e medir a distância do centro com o resto das coordenadas
e verificar se elas ultrapassam o raio.

'''
# Subprogramas

def calcula_Centro(alcance_lista, lista_de_posicoes): # Subprograma para Calcular o Centroide, recebe a lista e o tamanho da mesma

    centro = []
    for i in range(0,alcance_lista,1): # separa todas as as coodernas de X
        retax.append(float(lista_de_posicoes[i][0]))
    centro.append(sum(retax))

    for i in range(0,alcance_lista,1): # separa todas as as coodernas de Y
        retay.append(float(lista_de_posicoes[i][1]))
    centro.append(sum(retay))

    centro[0] = centro[0] / alcance_lista # Calcula a média
    centro[1] = centro[1] / alcance_lista # Calcula a média

    return centro

def calcula_distancia(tamanho_lista, centroide): # Retorna  os valores dentro da circunferência
    validos = []
    for i in range(tamanho_lista):
        distancia = sqrt((centroide[0] - retax[i])**2 + (centroide[1] - retay[i])**2) # Fórmula para calculo da distância
        if distancia < 6:
            validos.append(retax[i])
            validos.append(retay[i])
    return validos

def mostra_validos(validos):
    indice = 0
    for i in range(len(validos) - 2):
        print(validos[0 + indice], validos[1 + indice])
        indice += 2


# Programa Principal

retax = []
retay = []
lista_de_coordenadas = []
indice = 0
# Entrada e dados

entrada = input().split()
raio = int(entrada[0])
arquivo = open(entrada[1],'r')
linha = arquivo.readline()

while linha != "": # Adiciona cada linha do arquivo a uma lista
    lista_de_coordenadas.append(linha.split())
    linha = arquivo.readline()
arquivo.close()

tamanho_lista = len(lista_de_coordenadas) # Estabelece o tamanho da lista que estamos trabalhando
centroide = calcula_Centro(tamanho_lista, lista_de_coordenadas) # Calcula o centro geométrico

# Saida de Dados
print('Centroide: ({:.1f}, {:.1f})'.format(centroide[0],centroide[1]))
print('Listagem de Pontos dentro da Circunferência de Raio {}'.format(raio))

validos = calcula_distancia(tamanho_lista, centroide) # retorna as coordenadas válidas dentro do raio 6
mostra_validos(validos) # Exibe as coordenadas dentro da circunferência
