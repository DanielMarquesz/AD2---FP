
# Subprogramas

def dec4bin(num, binario): # Função Recursiva que retorna a conversão de números decimais para binários
    while num != 0:
        auxiliar = num % 2
        num = num // 2
        binario.append(auxiliar)
        return dec4bin(num, binario)
    print(binario[::-1])

def multiplicaNaturais(B,C,resultado): # Função Recursiva que retorna a multiplicação de 2 inteiros através da soma consecutiva de um deles
    if B == 0:
        print(resultado)
    else:
        B -= 1
        resultado += C
        return multiplicaNaturais(B, C, resultado)

def somaConsecutica(numero,total): # Função Recursiva que retorna a multiplicação de 2 inteiros através da soma consecutiva de um deles
    if numero == 0:
        return total
    else:
        total += 1/numero
        numero -= 1
        return somaConsecutica(numero,total)


# Progrma Principal

binario = [] # Declara uma lista vazia
numeroEntrada = int(input()) # Entrada do número a ser convertido
dec4bin(numeroEntrada,binario) # Chamada da função que imprime o número binário(Ignorando zeros à esquerda)

B, C = input().split() # Recebe dois valores inteiros
resultado = 0
B = int(B) # Converte os dois números para inteiros
C = int(C)
multiplicaNaturais(B,C,resultado) # Chamada da Função e Impressão dos números


total = 0
num = int(input()) # Entrada
if num > 0: # Verifica se o número é uma natural diferente de zero
    total = somaConsecutica(num,total) # Chamada da função e atribuição a variável
    print('{:.4f}'.format(total)) # Impressão do resultado formatado
else:
    pass
