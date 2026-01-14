import numpy as np

def mascara_ideal2D(M,N,fc):
    #M,N são as dimensões da imagem f(x,y) com domínio espacial, mas elas continuam com os mesmos valores M,N para o domínio na frequência
    H_ideal = np.zeros((M,N),dtype = complex)
    #No espectro de Fourier centralizado, a frequência zero fica no meio da imagem.
    #Se essa imagem tem M linhas, a distância do centro até a borda é M/2.
    ##LEMBRANDO: fc é normalizado, ou seja, está entre 0 e 1. Se eu quiser filtrar uma frequência de 2Hz, preciso colocar na fórmula fc = (f_desejada/f_maxima)
    #O filtro verifica a distância de cada ponto (u, v) até esse centro. Se a distância D(u, v) for menor ou igual a D0, a frequência "passa" (é multiplicada por 1); se for maior, ela é bloqueada (multiplicada por 0).

    D0 = fc*(M/2)
    #distância de cada pixel em relação ao centro da imagem
    for l in range(M):
        for c in range(N):
            dist_x = c - (N/2)
            dist_y = l - (M/2)
            #módulo das distâncias seria o raio em relação ao centro da imagem
            D = np.sqrt(dist_x**2 + dist_y**2)
            if D<=D0:
                H_ideal[l,c] = 1 + 0*(-1)**0.5 #coloca 1 se obedecer o if
    #H_ideal é complexo - criada como complex
    return H_ideal