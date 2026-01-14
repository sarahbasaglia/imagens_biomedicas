import numpy as np
import matplotlib.pyplot as plot
import cv2
from skimage import img_as_float
import skimage.exposure

#Lendo as imagens 
mamo = cv2.imread(r"C:\Users\sarah\Desktop\imagens_ biomedicas\aula2_transformacao_de_intensidade\Mamography.pgm", 0)
stent = cv2.imread(r"C:\Users\sarah\Desktop\imagens_ biomedicas\aula2_transformacao_de_intensidade\Stent.pgm", 0)

#Fazendo a normalização das imagens
mamoN = skimage.img_as_float(mamo)
stentN = skimage.img_as_float(stent)

#Exibir a imagem (mamogarfia)
plot.figure(0)
plot.ylabel('linha - M')
plot.xlabel('coluna - N')
plot.imshow(mamoN,cmap = 'gray')
plot.title('Mamografia 0')
plot.colorbar()
plot.show()

#Exibir a imagem (stent)
plot.figure(1)
plot.ylabel('M - linha')
plot.xlabel('N - Coluna')
plot.imshow(stentN,cmap = 'gray')
plot.title('Stent 0')
plot.show()

#Como obter o negativo: inversão dos valores de intensidade -> o que é branco fica preto e o que é preto fica branco.
#OBJETIVO GERAL: queremos percorrer cada pixel da imagem e criar UMA NOVA IMAGEM cujo valor em cada posição seja o negativo da imagem original.
(m,n) = np.shape(mamoN) #aqui vamos obter o tamanho da matriz
#Vamos criar duas matrizes: ambas precisam estar zeradas, pois uma receberá preenchida com o pixel da imagem e a outra vai recebero resultado do negativo.
mamoPixel = np.zeros((m,n), float) #por qual razão é do tipo float? Normalizamos a imagem, então os valores estão entre zero e 1.
mamoResultado = np.zeros((m,n),float)

for l in range(m): #percorre todas as linhas de (0 até M-1)
    for c in range(n): #percorre todas as colunas de 0 até N - 1
        mamoResultado[l,c] = 1 - mamoN[l,c]

#Exibindo imagem negativa
plot.figure(2)#o 1 é um identificador que faz com que cada imagem apareça em uma janela diferente.
plot.ylabel('Linhas')
plot.xlabel('Colunas')
plot.imshow(mamoResultado,cmap = 'gray')
plot.title('Mamografia negativada 1')
plot.colorbar()
plot.show()

#Criando uma operação para fazer o negativo, mas sem precisar fazer o loop.
mamoNegativo = 1 - mamoN
stentNegativo = 1 - stentN

#Mostrar mamo:
plot.figure(3)
plot.ylabel('Linhas')
plot.xlabel('Colunas')
plot.imshow(mamoNegativo,cmap = 'gray')
plot.colorbar()
plot.title('Mamografia Negativada 2')
plot.show()

#fazendo o histograma 
#importando a biblioteca 
import bibFuncoesHistograma

#chamar a função que vai retornar um vetor
histograma = bibFuncoesHistograma.fazer_histograma(mamo, m, n)
#plotar o histograma 
plot.figure(4)
plot.stem(histograma[5:255])
plot.ylabel('Número de ocorrência')
plot.xlabel('Número de Classes')
plot.title('Histograma mamografia 1')
plot.show()

#outra forma de fazer histograma:
histograma_2 = skimage.exposure.histogram(mamo)
x = histograma_2[1] #classes
y = histograma_2[0] #ocorrência 

plot.figure(5)
plot.stem(x[5:255], y[5:255])
plot.ylabel('Número de ocorrências')
plot.xlabel('Número de classes')
plot.title('Histograma mamografia 2')
plot.show()

## refazer o item anterior com as classes normalizadas entre 0 e 1. 
histograma_3 = skimage.exposure.histogram(mamoN)
x = histograma_3[1]
y = histograma_3[0]

plot.figure(6)
plot.stem(x[5:255],y[5:255])
plot.ylabel('Número de ocorrência')
plot.xlabel('Número de classes')
plot.title('Histograma mamografia Normalizada')
plot.show()

#aumento do brilho em mais de 0.2 níveis de intensidade(considerando ela entre 0 e -1)
histograma_2 = skimage.exposure.histogram(stentN)
x = histograma_2[1]
y = histograma_2[0]
plot.figure(7)
plot.stem(x,y)
plot.ylabel('Número de ocorrências')
plot.xlabel('Número de classes')
plot.title('Histograma Stent normalizado')
plot.show()

# Como colocar brilho?
stent_brilho = stentN + 0.2
#plotando figura
plot.figure(8)
plot.imshow(stent_brilho, cmap = 'gray')
plot.title('Stent brilho aumentado em 0.2 níveis.')
plot.show()

#quando queremos mudar o contraste dentro de uma faixa de intensidade 
#tudo que dor menor que 0.2 vira preto, w tudo que for maior que 0.7 vira branco. Os valores entre 0.2 e 0.7 são esticados
stent_alongado = skimage.exposure.rescale_intensity(stent_brilho,in_range=(0.2,0.7))
stent_gama = skimage.exposure.adjust_gamma(stent_alongado,1)#ainda não estamos mexendo não gama - ele continua igual a 1.
#plotando histograma imagem stent alongada
histograma_2 = skimage.exposure.histogram(stent_gama)
x = histograma_2[1]
y = histograma_2[0]
plot.figure(9)
plot.stem(x,y)
plot.ylabel('Número de ocorrências')
plot.xlabel('Número de classes')
plot.title('Histograma Stent alongado')
plot.show()
#plotando a imagem alongada
plot.figure(9)
plot.title('Stent gama')
plot.imshow(stent_gama, cmap = 'gray')
plot.show()