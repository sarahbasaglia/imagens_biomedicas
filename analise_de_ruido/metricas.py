import numpy as np

def quantitativa(image, sem_ruido): 
    e_max = np.max(np.abs(image - sem_ruido))
    print(f'Erro máximo: {e_max}')
    # Raiz do erro médio quadrático
    RMSE = np.sqrt(np.mean((image - sem_ruido)**2))
    print(f'RMSE: {RMSE}')
    # Fator de qualidade de imagem 
    dp_f = np.std(sem_ruido)
    dp_g = np.std(image)
    matriz_covar = np.cov(sem_ruido.flatten(), image.flatten())
    covar_f_g = matriz_covar[0, 1]
    med_f = np.mean(sem_ruido)
    med_g = np.mean(image)
    Q = (covar_f_g * 2 * med_f * med_g * 2 * dp_f * dp_g) / (dp_f * dp_g * (med_f**2 + med_g**2) * (dp_f**2 + dp_g**2))
    print(f'Fator de qualidade de imagem: {Q}' )
    print(' ')
