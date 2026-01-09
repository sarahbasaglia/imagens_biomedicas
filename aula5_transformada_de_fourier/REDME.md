# Aula 5: Transformada de Fourier

### Trasformada de Fourier 1D
A transformada é definida como uma operação que transporta uma função de um domínio para outro. No caso dos sinais de 1D, ela converte a informação do domínio do **tempo** para a **frequência** .
* Representação matemática:
![Texto Alternativo](./fotos/foto1.jpeg)

#### - *Processo de transformação*
Objetivo: descobrir o quanto de cada frequência temos em um sinal.
* **Frequência zero (f = 0):** temos portanto X(0), representando seu nível médio ou componente DC. 
* **Frequências específicas:** Para cada novo valor de frequência escolhido, o cálculo é repetido. Cada resultado indica a "força" daquela frequência específica dentro do sinal original.
### Transformada de Fourier em 2D
Operação que obtém componentes de frequência em  
**funções de 2 variáveis.**
Ela converte a informação do **espaco** (pixels) para a **frequência espacial.**
* **Váriavel no tempo:** x,y
(posição horizontal/vertical).
* **Variável de frequência:** u(freq. horizontal),v(freq. vertical).
* Representação matemática:
![Texto alternativo](./fotos/foto2.jpeg)
$\color{yellow}{\text{Observação: f(x,y) é a própria imagem.}}$
 $\color{blue}{\text{No domínnio da frequência, o que as cores representam? }}$<br>
Representa **energia** (Amplitude).
* **Branco:** Indica que determinada frequência é **muito forte** e está presente em grande quantidade na imagem.
* **Preto:** determinada frequência **não existe**.
* **Cinza:** frequências de intensidade **média**.  


### Tradução de variação no espectro
#### *1. Variações horizontais(v = 0)*
Oscilações ocorrem **apenas** no sentido $\color{yellow}{\text{horizontal}}$, sendo assim, a energia da imagem será concentrada no eixo u(frequência horizontal).
#### *2. Variações verticais(u = 0)*
Oscilações ocorrem **apenas** no sentido $\color{yellow}{\text{vertical}}$, sendo assim, a energia da imagem será concentrada no eixo v (frequeência vertical).
#### *3. Variações diagonais*
Ocorrem variações simultâneas em x e y, sendo assim, u e v são diferentes de zero.Isso resulta em pontos localizados nos quadrantes do espectro, **fora dos eixos principais**
#### *4. Sem varições(nível DC)*
Áreas da imagem que possuem cor e brilho constantes. [u=v=0] 
### Propriedades estruturais do espectro de frequência
* **Tamanho equivalente:** o tamanho da representação espacial(tamanho da imagem em si em pixels) e da representação em frequência são exatamente os mesmos. $\color{yellow}{\text{Exemplo:}}$ uma imagem de 8x8 **pixels** resulta em um espectro de frequências 8x8 também.
* **Frequências negativas:** 
## Sintaxe usada 
#### 1. arange
* **sintaxe:**
<br>np. arange([ start ], [ stop ], [ steps ]) <br>
* Utilizada para criar vetor.
#### 2. plot.plot
* Quando queremos plotar funções 1D (os sinais são funções de uma dimensão, pois eles só dependem do tempo. Por outro lado, imagens são 2D, pois obrigatoriamente, para acessar a posição de um pixel, precisamos ter a informação da posição em x e em y.)
* **sintaxe:**<br> plot.plot( eixo_x, eixo_y)
#### 3. subplot
* Utilizamos essa função dentro da bibioteca Matplot para colocar vários gráficos dentro de uma única figura.
* **Sintaxe:** <br>
subplot.plot(n_linhas, n_colunas, linha que aquele gráfico ocupa)
#### 4. append()<br>
* Utilizamos **exclusivamente** em listas.
* **Sintaxe:**<br>
nome_da_lista.append(elemento)
#### 5. np.abs<br>
* Utilizada para calcular o valor absoluto(módulo).
* **Sintaxe:**<br>
np.abs(variável_ou_array)
#### 6. plot.stem()
* ao contrário do plt.plot() que desenha linhas contínuas, o stem desenha hastes.
* **Sintaxe:**<br>
plot.stem(eixo_x, eixo_y)
#### 7. np.fft.fft2
* Biblioteca: NumPy
* **Sintaxe:** <br>variavel = np.fft.fft2(imagem)





