
raio, dados = input().split()

abertura = open(dados,'r')
coordenadas = abertura.readline()


lista = []

while coordenadas != '':
    lista.append(coordenadas)
    del lista[8:10]
    coordenadas = abertura.readline()


print(lista)
