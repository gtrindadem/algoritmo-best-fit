# Guilherme Trindade Mendes
# RA: F045FB-0  Turma: CC6P12

import random

tamanhoDaMemoria = 100 # Altere essa variavel para definir o tamanho da memoria a ser trabalhada
menorTamanhoDeProcesso = 1 # Altere essa variavel para definir o menor tamanho possivel de um processo
maiorTamanhoDeProcesso = 5 # Altere essa variavel para definir o maior tamanho possivel de um processo

memoria = [0] * tamanhoDaMemoria
processosAtuais = []
idProcessoAtual = 0

def criaNovoProcesso():
    global processosAtuais
    global idProcessoAtual

    idProcessoAtual += 1
    processosAtuais.append(idProcessoAtual)
    tamanhoProcesso = random.randrange(menorTamanhoDeProcesso, maiorTamanhoDeProcesso + 1);

    return { "id": idProcessoAtual, "tamanho": tamanhoProcesso }

def encontraMelhorIndex(tamanhoNecessario):
    indiceParaInsercao = -1
    menorIntervaloEncontrado = tamanhoDaMemoria + 1
    intervaloAberto = 0

    for i in range(tamanhoDaMemoria):
        if memoria[i] == 0:
            intervaloAberto += 1
        else:
            if intervaloAberto != 0 and intervaloAberto >= tamanhoNecessario and intervaloAberto < menorIntervaloEncontrado:
                menorIntervaloEncontrado = intervaloAberto
                indiceParaInsercao = i - intervaloAberto
            intervaloAberto = 0
    
    if intervaloAberto != 0 and intervaloAberto >= tamanhoNecessario and intervaloAberto < menorIntervaloEncontrado:
        menorIntervaloEncontrado = intervaloAberto
        indiceParaInsercao = tamanhoDaMemoria - intervaloAberto

    if menorIntervaloEncontrado != (tamanhoDaMemoria + 1):
        print('MENOR ESPACO POSSIVEL:', menorIntervaloEncontrado)
    else:
        print('NÃO HA ESPACO SUFICIENTE')
    
    return indiceParaInsercao
            

def alocaNaMemoria(index, processo):
    for i in range(processo['tamanho']):
        memoria[index + i] = processo['id']

def desalocaNaMemoria():
    global processosAtuais

    idRandomico = random.choice(processosAtuais)
    processosAtuais.remove(idRandomico)

    for i, j in enumerate(memoria):
        if j == idRandomico:
            memoria[i] = 0

    print('REMOVIDO ID', idRandomico);
    print('MEMORIA', memoria)
    print('---------------------------------')


## EXECUCAO ##

print('## INICIO ##')
print('MEMORIA', memoria)
print('---------------------------------')

while (True):
    processo = criaNovoProcesso()
    print('NOVO PROCESSO:', processo)

    index = encontraMelhorIndex(processo['tamanho'])
    print('MELHOR INDEX:', index)

    if index == -1:
        print('## FIM ##')
        break

    alocaNaMemoria(index, processo)
    print('INSERIDO');
    print('MEMORIA', memoria)
    print('---------------------------------')

    if idProcessoAtual % 2 == 0:
        desalocaNaMemoria()
