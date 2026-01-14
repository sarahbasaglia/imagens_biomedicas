import numpy as np
import matplotlib.pyplot as plot
import cv2
import skimage
import skimage.exposure
import scipy.signal

def fazerKernelGauss2D(media, desvio):
    #nete laboratório,, o kernel deve ter o tamanho da amostra. O tamanho da minha amostra será computado como(tamanho = (2*media)+1)
    tamanho = (2*media)+1 #tamanho da amostra
    #o vetor g representa a nossa distribuição gaussiana unidimensional. 
    gauss = scipy.signal.windows.gaussian(tamanho, std=desvio)

    #as 4 linhas de código abaixo geram a máscara quadrada.
    #matriz nula com o tamanho da nossa amostra
    g1 = np.zeros((tamanho,tamanho), float)
    # na linha onde a nossa média está, vamos colocar o vetor gaussiano g na horizonal
    g1[media,:] = gauss
    #com a transposta de g1 temos os elementos na horizontal.
    g1_transposta = np.transpose(g1)
    convolucao_gaussiana = scipy.signal.convolve2d(g1,g1_transposta, 'same')
    #normalização
    norm = convolucao_gaussiana/np.sum(convolucao_gaussiana)
    return norm