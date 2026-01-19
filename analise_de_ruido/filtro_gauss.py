import numpy as np

def gaussiana(M,N,fc):
    H_gauss = np.zeros((M,N), complex)
    Do = fc*(M/2)
    #Distância 
    for m in range(M):
        for n in range(N):
            dist_x = n - (N/2)
            dist_y =  m - (M/2)
            D = ((dist_x**2 + dist_y**2)**0.5)
            #Gauss - fórmula
            H_gauss[m,n] = np.exp(-0.5*((D**2)/Do**2))
    return H_gauss
