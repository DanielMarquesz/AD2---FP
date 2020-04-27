
def separaNomeclatura(dados): # Separa o CPF e o Nome do vírus

    nome = dados.split('#')
    nomeDefinido = nome[0]

    return  nomeDefinido

def separaMaterial(dna): # Função para separar o RNA e DNA da nomeclatura e separar as strings

    virusRna = dna.split('#')
    RNA = virusRna[1]
    RNA = list(RNA)

    return  RNA

def verificaVirus(DNA, RNA): # Verifica se a pessoa está infectada

    count = 0
    for i in range(len(RNA)):
        if DNA[i] == RNA[i]:
            count += 1

    return count


dadosVirus = open('virus.txt','r') # Abre o arquivo de texto com os dados do vírus
dadosPopulacao = open('populacao.txt','r') # Abre o arquivo de texto com os dados da população

virusRna = dadosVirus.readline()
populacaoDna = dadosPopulacao.readline()

nomeVirus = separaNomeclatura(virusRna) # Separa o nome do paciente e seu DNA
cpfPaciente = separaNomeclatura(populacaoDna) # Separa o nome do paciente e seu RNA

DNA = separaMaterial(populacaoDna) # Separa as letras das strings do DNA
RNA = separaMaterial(virusRna)     # Separa as letras das strings do RNA

nucleosBase = verificaVirus(DNA, RNA) # Retorna a Quantidade de núcleos em comum com o vírus

if nucleosBase > 11:
    print('O CPF {} está infectado com o vírus {},'
          ' pois tem igualdade de núcleos base em {} de 22 Posições.'.format(cpfPaciente,nomeVirus,nucleosBase))

else:
    print('O CPF {} não está infectado com o vírus {},'
          ' pois tem igualdade de núcleos base em {} de 22 Posições.'.format(cpfPaciente,nomeVirus,nucleosBase))

dadosVirus.close() # Fecha o arquivo de texto
dadosPopulacao.close() # Fecha o arquivo de texto
