# Filtro de Lee
## Objetivo
Entender como reduzir ruídos em imagens sem perder os detalhes importantes, como as bordas. 
## 1. Filtro média
É uma técnica de **suavização** simples, em que o valor do pixel central da máscara é substituído pela média aritmética das intensidades de todos os pixels ao seu redor. 

* **Efeito do tamanho do kernel:** quanto maior o kernel, maior é o efeito de suavização, mas também maior é o borrão. 
* **Desvantagem:** o filtro média é um filtro **passa-baixa**, então ele prejudica as bordas da imagem, tornando-as borradas e menos definidas.
## 2. Filtro de Lee
O filtro de Lee surge como uma solução para o problema das bordas. Ele age como um filtro **adaptativo**, ou seja, ele age diferente dependendo da região da imagem a qual o kernel está posicionado.
### Coeficiente k
Identifica se a região é homogênea(região de tecido) ou se possui borda.
* **Região Homogênea( k ≈ 0):** Filtro se comporta como um filtro média, suavizando o ruído.
* **Região com borda ( k ≈ 1):** filtro preserva valor do pixel, minimizando efeito do borrão e mantendo a nitidez da borda.

* **Fórmula:**
 $$k = 1 - \frac{varRegHomogenia}{varLocal}$$
 Componentes: 
* **Variância da Região Homogênea:** É a medida de dispersão dos dados em uma área onde não existem bordas ou estruturas. 
* **Variância Local:**

O kernel percorre a imagem e em cada janela, a variância entre os pixels é calculada. Ela fornece o quanto os valores dos pixels variam em relação à média. Se a variância é baixa, tem-se uma região **homogênea**. Se a variância é alta, é uma região de **borda**.
### Fórmula filtro de Lee
$$I_{Lee}(x,y) = \text{média} + k \cdot (I(x,y) - \text{média})$$
* I: valor original do pixel(imagem original). 
* média: média local calculada no kernel.
* k: peso que varia entre 0 e 1, o que depende se a região é homogênea ou borda. 
## Funções utilizadas 
* Biblioteca **openCV**.
* Ela permite que o usuário selecione manualmente uma **região de interesse (ROI - Region of Interest)** em uma imagem.
* **Sintaxe:**

roi = cv2.selectROI(img)
* **Retorno:** Uma tupla com 4 valores inteiros (x, y, w, h)

 x: Coordenada horizontal do canto superior esquerdo.

y: Coordenada vertical do canto superior esquerdo.

w: Largura do retângulo.

h: Altura do retângulo.

