# Processamento de Imagens Biomédicas

Este repositório contém os estudos teóricos e práticos sobre o processamento de imagens médicas.

## 📚 Conteúdo das Aulas

### Aula 04: Máscaras para Filtragem e Restauração
Nesta aula, focamos na remoção de ruídos em exames de Ressonância Magnética (MRI).

#### Teoria: Filtros de Suavização
Os filtros espaciais são fundamentais para melhorar a qualidade da imagem antes da análise diagnóstica:

* **Filtro de Média:** Substitui o valor do pixel pela média aritmética da vizinhança. Útil para ruídos uniformes.
* **Filtro de Mediana:** Substitui o valor pelo valor central da vizinhança ordenada. É o método mais eficaz para eliminar o ruído **"Sal e Pimenta"**, como o encontrado no arquivo `TransversalMRI_salt-and-pepper.pgm`.

#### Equação Base (Convolução)
A aplicação das máscaras segue a operação matemática de convolução:
$$g(x,y) = \sum_{s=-a}^{a} \sum_{t=-b}^{b} w(s,t) f(x+s, y+t)$$