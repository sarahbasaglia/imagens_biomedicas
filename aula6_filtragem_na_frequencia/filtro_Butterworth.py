import numpy as np

def butter(M,N,fc,n):
    H_butter = np.zeros((M,N), complex)
    Do = fc*(M/2)
    #Distância 
    for l in range(M):
        for c in range(N):
            dist_x = c - (N/2)
            dist_y = l - (M/2)
            D = ((dist_x**2 + dist_y**2)**0.5)
            #Butter - fórmula
            H_butter[l,c] = 1 / (1+((D/Do)**2*n))
    return H_butter
