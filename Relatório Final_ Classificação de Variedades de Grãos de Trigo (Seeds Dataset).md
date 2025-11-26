# Relatório Final: Classificação de Variedades de Grãos de Trigo (Seeds Dataset)

## 1. Introdução e Objetivo

Este projeto visa automatizar a classificação de variedades de grãos de trigo, um processo tradicionalmente manual em cooperativas agrícolas de pequeno porte, que é propenso a erros e demorado. A metodologia **CRISP-DM** (Cross-Industry Standard Process for Data Mining) foi aplicada para desenvolver um modelo de aprendizado de máquina capaz de distinguir três variedades de grãos de trigo: **Kama**, **Rosa** e **Canadian**, com base em suas características físicas.

O conjunto de dados utilizado é o **Seeds Dataset** do UCI Machine Learning Repository, que contém 210 amostras de grãos de trigo, 70 de cada variedade, com 7 atributos geométricos: Área, Perímetro, Compacidade, Comprimento do Núcleo, Largura do Núcleo, Coeficiente de Assimetria e Comprimento do Sulco do Núcleo.

## 2. Preparação e Análise Exploratória dos Dados

O dataset foi carregado a partir de um arquivo de texto, pois a API `ucimlrepo` não estava disponível para importação direta.

### 2.1. Inspeção Inicial e Estatísticas Descritivas

O conjunto de dados não apresentou valores ausentes e todas as 7 características são do tipo `float64`, adequadas para modelagem. A contagem de classes é perfeitamente balanceada, com 70 instâncias para cada uma das três variedades (Kama, Rosa, Canadian).

As estatísticas descritivas revelaram que as características possuem escalas variadas, o que justifica a necessidade de padronização para algoritmos baseados em distância (como KNN e SVM).

| Característica | Média | Desvio Padrão | Mínimo | Máximo |
| :--- | :--- | :--- | :--- | :--- |
| Area | 14.85 | 2.91 | 10.59 | 21.18 |
| Perimeter | 14.56 | 1.31 | 12.41 | 17.25 |
| Compactness | 0.871 | 0.024 | 0.808 | 0.918 |
| Length\_of\_kernel | 5.63 | 0.44 | 4.899 | 6.675 |
| Width\_of\_kernel | 3.26 | 0.38 | 2.63 | 4.033 |
| Asymmetry\_coefficient | 3.70 | 1.50 | 0.765 | 8.456 |
| Length\_of\_kernel\_groove | 5.41 | 0.49 | 4.519 | 6.55 |

### 2.2. Análise de Correlação

A matriz de correlação indicou uma **alta correlação positiva** entre a maioria das características geométricas (e.g., Área, Perímetro, Comprimento e Largura do Núcleo), o que é esperado para medições de formato. A característica **Compactness** (Compacidade) mostrou uma correlação negativa com o **Asymmetry\_coefficient** (Coeficiente de Assimetria).

### 2.3. Pré-processamento

Os dados foram divididos em conjuntos de treinamento (70%) e teste (30%), com estratificação para manter a proporção de classes. Em seguida, foi aplicada a **Padronização (StandardScaler)** para transformar os dados, garantindo que todos os atributos contribuam igualmente para os modelos baseados em distância.

## 3. Modelagem e Avaliação Inicial

Quatro algoritmos de classificação foram implementados e avaliados no conjunto de teste (30% dos dados): K-Nearest Neighbors (KNN), Support Vector Machine (SVM), Random Forest e Regressão Logística.

A tabela a seguir resume o desempenho dos modelos base (antes da otimização), utilizando métricas macro-médias (Macro Avg) para garantir que o desempenho em cada classe seja considerado igualmente.

| Modelo | Acurácia | Precisão (Macro) | Recall (Macro) | F1-Score (Macro) |
| :--- | :--- | :--- | :--- | :--- |
| **Random Forest** | **0.9524** | **0.9524** | **0.9524** | **0.9524** |
| KNN | 0.9365 | 0.9365 | 0.9365 | 0.9365 |
| Regressão Logística | 0.9048 | 0.9048 | 0.9048 | 0.9048 |
| SVM | 0.8571 | 0.8571 | 0.8571 | 0.8571 |

O modelo **Random Forest** demonstrou o melhor desempenho inicial, alcançando uma acurácia e F1-Score de **95.24%**.

## 4. Otimização dos Modelos

A otimização de hiperparâmetros foi realizada no modelo **SVM** (que se beneficia significativamente da padronização) usando `GridSearchCV` com validação cruzada (cv=5) e o F1-Score macro como métrica de pontuação.

Os melhores hiperparâmetros encontrados para o SVM foram: `{'C': 100, 'gamma': 'scale', 'kernel': 'linear'}`.

### 4.1. Desempenho do Modelo Otimizado (SVM)

O modelo SVM otimizado alcançou os seguintes resultados no conjunto de teste:

*   **Acurácia:** 0.8889
*   **F1-Score (Macro):** 0.8875

A otimização melhorou o desempenho do SVM (de 85.71% para 88.89% de acurácia), mas o modelo **Random Forest Base** (95.24% de acurácia) permaneceu o mais robusto.

## 5. Interpretação e Insights Relevantes

### 5.1. Modelo Recomendado

O modelo **Random Forest Base** é o mais recomendado para a classificação dos grãos, devido ao seu desempenho superior (Acurácia e F1-Score de 95.24%) em comparação com os outros modelos, incluindo o SVM otimizado.

### 5.2. Importância das Características

A análise de importância de features do modelo Random Forest revelou quais características são mais cruciais para a distinção das variedades:

| Feature | Score de Importância |
| :--- | :--- |
| **Length\_of\_kernel\_groove** | **0.29** |
| **Compactness** | **0.23** |
| Area | 0.16 |
| Length\_of\_kernel | 0.13 |
| Width\_of\_kernel | 0.09 |
| Asymmetry\_coefficient | 0.05 |
| Perimeter | 0.05 |

As características **Comprimento do Sulco do Núcleo** e **Compacidade** são, de longe, as mais importantes para a classificação. Isso sugere que o foco na medição precisa dessas duas propriedades geométricas é crucial para a classificação automatizada.

### 5.3. Separação de Classes e Matriz de Confusão

A análise exploratória e os resultados dos modelos indicam que as variedades são **Facilmente** separáveis no espaço de features, o que explica o alto desempenho dos modelos.

A maior confusão observada nos modelos menos performáticos (como o SVM otimizado) ocorreu entre as variedades **Rosa** e **Canadian**, enquanto a variedade **Kama** foi consistentemente bem classificada.

## 6. Conclusão

O projeto demonstrou que o aprendizado de máquina é altamente eficaz para automatizar a classificação de grãos de trigo, superando a classificação manual em termos de precisão. O modelo **Random Forest** é a solução ideal, atingindo uma acurácia de 95.24% no conjunto de teste.

**Recomendação:** O modelo Random Forest, treinado com os dados padronizados, deve ser implementado em um sistema de classificação automatizado para aumentar a eficiência e reduzir erros humanos na cooperativa agrícola. O foco na medição precisa do **Comprimento do Sulco do Núcleo** e da **Compacidade** deve ser priorizado, pois são as características mais discriminatórias.

---
**Anexos:**
1.  `seeds_classification_executed.ipynb`: Notebook Jupyter/Colab com todo o código executado, análises e visualizações.
2.  `seeds_dataset.txt`: O conjunto de dados original utilizado.
3.  Imagens geradas durante a execução do notebook (histogramas, boxplots, matrizes de correlação e confusão, e importância de features).
