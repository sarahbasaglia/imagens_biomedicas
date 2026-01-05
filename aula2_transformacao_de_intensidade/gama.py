import numpy as np
import matplotlib.pyplot as plot
import cv2
from skimage import img_as_float
import skimage.exposure

#lendo a imagem
stent = cv2.imread(r"C:\Users\sarah\Desktop\imagens_ biomedicas\aula2_transformacao_de_intensidade\Stent.pgm", 0)

#normalizando 
stentN = skimage.img_as_float(stent)

plot.figure(0)
plot.title('Stent normalizado')
plot.imshow(stentN, cmap = 'gray')
plot.show()

#vamos mexer no gama 
stent_gama = skimage.exposure.adjust_gamma(stentN,1) #para mexer nos valores de gama, é só mexer no 1
plot.figure(1)
plot.title('Imagem stent gama')
plot.imshow(stent_gama, cmap = 'gray')
plot.show()