
M = [1,5,6,2,3,0,4]

menores = []
div = len(M)// 2 # Elemento V[i]

for i in range(7): # tamanho da lista
    if M[i] < 3:
        menores.append(M[i])

M = [1,5,6,2,3,0,4]

menores := [] # Novo vetor com os elementos menores que [n/2]
comprimentodaLista := tamanho(M) # Atribui a variável o tamanho da lista
elementoMedio := comprimentodaLista // 2 # Realiza uma divisao inteira do comprimento da lista fornecida

para i := 0 até comprimentodaLista:
    se M[i] < elementoMedio:
        menores += M[i]
