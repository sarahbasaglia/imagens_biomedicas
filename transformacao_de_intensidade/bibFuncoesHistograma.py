#fazer uma função que retorna um vetor hisstograma com 256 posições, contendo a contagem de pixel para cada intensidade
def fazer_histograma(imagem , x, y):
    import numpy as np
    #declarando vetor histograma: inicialmente vazio 
    histograma = np.zeros((256), int)#int pois recebe todos os valores de inteiros
    for l in range(x):
        for c in range(y):
            histograma[imagem[l,c]] = histograma[imagem[l,c]] + 1 #coloca 1 na caixinha do vetor sempre que encontra um pixel de uma determinada intensidade.
    return histograma