#CORRELAÇÃO, CONVOLUÇÃO E KERNEL

#%%QUESTÃO 1: fazer dois vetores
import numpy as np

w = np.array([1,2,3,2,8]) # em Python não existe vetores. A estrutura (lista = [x,y,z]) funciona como lista, e não como vetor. Então usamos o array para trabalhar com vetores. #kernel
f = np.array([0,0,0,1,0,0,0,0])#sinal

print(f"Vetor 1: {w}, vetor 2: {f}")
# criar um vetor preenchido com zeros de tamanho 4. Como o vetor do nosso sinal possui 5 números, então nosso vetor de preenchimento de 0 terá tamanho 4.
pad = np.zeros((4),int) #se fosse (1,4) está relacionado ao tamanho da matriz: Uma matriz com 1 linha e 4 colunas. 

#FUNÇÃO CONCATENATE: ela junta dois ou mais arrays em um único array.
#Sintaxe clássica: np.concatenate((array1, array2, ...), axis = 0)
#axis = 0(ou axis = None): vetor array2 colocado abaixo de array1.
#axis = 1: vetor array2 é colocado do lado de array1.
fpadding = np.concatenate((pad,f,pad), axis = 0)
print(fpadding)

#%%QUESTÃO 2
#Vamos utilizar a função np.shape para achar o tamanho dos vetores.
# Para usar a função np. shape, na primeira casa do vetor temos o número de linhas da matriz; na segunda, ele nps irá fornecer o número de colunas. Neste caso, como estamos lidando apenas com vetores, deixar o lugar do y sem nada. 
(Lf, ) =  np.shape(f) 
(Lw, ) = np.shape(w)
(L, ) = np.shape(fpadding) #L = Lo + 2*(Lw - 1)

for i in range(L): #a variável i vai até o tamanho de L.
    fpadding[i]

# ATENÇÃO: para a questão 3 e 4 vamos fazer a mesma coisa, porém de formas diferentes.
#%%Questão 3: operação de correlação cruzada. 
L_correlacao = Lf + (Lw - 1) #Comprimenrto do vetor de correlação cruzada. 
cor = np.zeros(L_correlacao, int) #criar um vetor nulo do tamanho da correlação cruzada. 

for i in range(L_correlacao):
# O que é um slicing em Python?[start,stop] Ele é utilizado para pegar "um pedaço" de uma lista ou de um array; O vetor w = [1,2,3,2,8] , então 1 está na posição 0, 2 está na posição 1, e assim por diantes. O stop neste caso é o tamanho de w, que é LW. 
    cor[i] = np.sum(w[0:Lw ] * fpadding[i:i+5])
#quando i = 0, fpadding[0:0+5], ou seja, vai pegar o elemento de fpadding que vai de 0 até 4. Resultado: [0,0,0,0,0]

#%% Questão 4: utilize a função np.correlate para verificar o resultado.
#Sintaxe da função: np.correlate(a, v,mode = 'full')
# O primeiro vetor é o seu sinal( no nosso cado, o f); o segundo vetor será nosso kernel( o nosso w).
cor_function1 = np.correlate(f,w, mode = "full")
print(f"Vetor pela função np.correlate: {cor_function1}")

#%%Questão 5: Recorte o início e o fim do vetor do resultado Final cor, para que este tenha o tamanho do sinal original de f ou seja, 8 posições. 
# quero que meu vetor final tenha 8 posições( o mesmo tamanho que o meu sinal.)
#vou criar um vetor com 8 posições que será utilizado para armazenar o meu vetor "cortado".
corte = np.zeros(8, int)
corte[0:7] = cor[2:9]

#%%Questão 6
#criar uma matriz f e outra c de 5 linhas e 5 colunas.
matriz = np.zeros((5,5),float) #sinal
#acessar a posição (2,2) e colocar 1;
matriz[2,2] = 1
print(f"Matriz f:\n {matriz}")
(M,N) = np.shape(matriz)
print(f"Número de linhas e colunas: {M,N}")

#a matriz c possui valores espcíficos, dado para a gente no enunciado 
kernel = np.array([[1,2,3],[4,5,6],[7,8,9]]) #kernel

#%% Questão 7 # estutura chamada célula de código 
#Faça uma função de correlação 2D entre a matriz "matriz "que criamos com a mascara w, usando apenas 2 for
cor_function2 = np.zeros((3,3), float)
for l in range(3):
    for c in range(3):
        cor_function2[l,c] = np.sum((kernel[0:3 , 0:3] * matriz [l:l+3, c: c+3]))
#matriz [l:l+3, c: c+3] aqui temos o slicing: comece no l e vai até o l+3 nas linhas; a mesma coisa aplica para coluna.
print(f"Cor_function2:\n {cor_function2}")

#%% Questão 9
