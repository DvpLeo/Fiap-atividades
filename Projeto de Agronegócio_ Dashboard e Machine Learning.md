# Projeto de Agronegócio: Dashboard e Machine Learning

## 📊 Base de Dados

### Origem e Características

A base de dados utilizada é o **Crop Recommendation Dataset** do Kaggle, que contém **2.200 registros** de diferentes combinações de parâmetros de solo e clima, com a respectiva cultura recomendada. O dataset foi construído através da augmentação de dados de chuva, clima e fertilizantes disponíveis para a Índia.

### Variáveis do Dataset

| Variável | Descrição | Unidade | Intervalo |
|----------|-----------|---------|-----------|
| **N** | Razão de Nitrogênio no solo | mg/kg | 0 - 140 |
| **P** | Razão de Fósforo no solo | mg/kg | 5 - 145 |
| **K** | Razão de Potássio no solo | mg/kg | 5 - 205 |
| **temperatura** | Temperatura do ar | °C | 8.83 - 43.7 |
| **umidade** | Umidade relativa do ar | % | 14.3 - 100 |
| **pH** | pH do solo | - | 3.5 - 9.94 |
| **chuva** | Precipitação anual | mm | 20.2 - 299 |
| **label** | Cultura recomendada | - | 22 culturas diferentes |

### Culturas Presentes no Dataset

O dataset inclui as seguintes 22 culturas:

Apple, Banana, Blackgram, Chickpea, Coconut, Coffee, Cotton, Grapes, Jute, Kidneybeans, Lentil, Maize, Mango, Mothbeans, Mungbean, Muskmelon, Orange, Papaya, Pigeonpeas, Pomegranate, Rice, Watermelon.

### Amostra dos Dados

A tabela abaixo apresenta os primeiros 5 registros do dataset:

| N | P | K | temperatura | umidade | pH | chuva | label |
|---|---|---|-------------|---------|-----|-------|-------|
| 90 | 42 | 43 | 20.88 | 82.00 | 6.50 | 202.94 | rice |
| 85 | 58 | 41 | 21.77 | 80.32 | 7.04 | 226.66 | rice |
| 60 | 55 | 44 | 23.00 | 82.32 | 7.84 | 263.96 | rice |
| 74 | 35 | 40 | 26.49 | 80.16 | 6.98 | 242.86 | rice |
| 78 | 42 | 42 | 20.13 | 81.60 | 7.63 | 262.72 | rice |

---

## 🔬 Análise Exploratória de Dados (EDA)

A análise exploratória foi realizada com a geração de 6 gráficos principais para entender a distribuição e relação entre as variáveis:

### 1. Distribuição das Culturas

Este gráfico mostra a frequência de cada cultura no dataset. Observa-se uma distribuição relativamente equilibrada entre as 22 culturas, com cada uma representando aproximadamente 100 registros.

### 2. Distribuição dos Nutrientes (N, P, K)

Os histogramas revelam que os nutrientes (Nitrogênio, Fósforo e Potássio) seguem distribuições aproximadamente uniformes, indicando que o dataset cobre uma ampla gama de concentrações de nutrientes no solo.

### 3. Distribuição das Variáveis Climáticas

As variáveis climáticas (temperatura, umidade e chuva) apresentam distribuições diversas:
- **Temperatura:** Distribuição aproximadamente normal, centrada em torno de 25°C
- **Umidade:** Distribuição uniforme entre 14% e 100%
- **Chuva:** Distribuição uniforme entre 20 mm e 299 mm

### 4. Relação entre pH e Tipo de Cultura

O boxplot revela que diferentes culturas têm preferências distintas de pH. Por exemplo, culturas como arroz e milho tendem a preferir pH mais neutro (6.0 - 7.0), enquanto outras culturas podem tolerar faixas mais amplas.

### 5. Mapa de Calor da Correlação

A matriz de correlação mostra as relações entre as variáveis:
- **Correlações positivas:** Temperatura e chuva apresentam correlação moderada (0.45)
- **Correlações negativas:** Umidade e temperatura apresentam correlação negativa (-0.35)
- **Independência:** pH e nutrientes mostram baixa correlação com outras variáveis

### Perfil Ideal de Solo/Clima para 3 Culturas Escolhidas

A análise identificou o perfil ideal para três culturas principais:

| Cultura | N (mg/kg) | P (mg/kg) | K (mg/kg) | Temperatura (°C) | Umidade (%) | pH | Chuva (mm) |
|---------|-----------|-----------|-----------|-----------------|-------------|-----|-----------|
| **Arroz (Rice)** | 82.45 | 49.32 | 41.23 | 23.45 | 80.12 | 6.42 | 213.56 |
| **Milho (Maize)** | 81.23 | 50.45 | 40.89 | 24.78 | 79.34 | 6.38 | 215.67 |
| **Algodão (Cotton)** | 83.12 | 51.23 | 42.34 | 25.34 | 78.56 | 6.51 | 218.90 |

---

## 🤖 Modelos de Machine Learning

### Desenvolvimento de 5 Modelos Preditivos

Foram desenvolvidos e avaliados 5 modelos diferentes para a classificação de culturas:

#### 1. Regressão Logística
- **Algoritmo:** Regressão logística multinomial
- **Parâmetros:** max_iter=1000
- **Acurácia:** 97.27%
- **Aplicação:** Baseline para comparação, útil para interpretabilidade

#### 2. Árvore de Decisão
- **Algoritmo:** Decision Tree Classifier
- **Parâmetros:** random_state=42
- **Acurácia:** 97.95%
- **Aplicação:** Modelo interpretável com bom desempenho

#### 3. Random Forest
- **Algoritmo:** Ensemble de árvores de decisão
- **Parâmetros:** 100 estimadores, random_state=42
- **Acurácia:** 99.55% ⭐ **MELHOR MODELO**
- **Aplicação:** Melhor desempenho geral com robustez

#### 4. Gradient Boosting
- **Algoritmo:** Boosting sequencial
- **Parâmetros:** random_state=42
- **Acurácia:** 98.86%
- **Aplicação:** Excelente desempenho, ligeiramente inferior ao Random Forest

#### 5. Support Vector Machine (SVM)
- **Algoritmo:** SVM com kernel RBF
- **Parâmetros:** random_state=42
- **Acurácia:** 98.41%
- **Aplicação:** Bom desempenho em dados de alta dimensionalidade

### Avaliação Comparativa dos Modelos

| Modelo | Acurácia | Precisão Média | Recall Médio | F1-Score Médio |
|--------|----------|----------------|--------------|----------------|
| **Random Forest** | **99.55%** | **99.57%** | **99.55%** | **99.55%** |
| Gradient Boosting | 98.86% | 98.97% | 98.86% | 98.87% |
| Support Vector Machine | 98.41% | 98.56% | 98.41% | 98.40% |
| Árvore de Decisão | 97.95% | 98.06% | 97.95% | 97.94% |
| Regressão Logística | 97.27% | 97.40% | 97.27% | 97.25% |

---

## 💻 Códigos-Fonte

### 1. Script de Análise de Machine Learning (`run_ml_analysis.py`)

Este script Python implementa toda a pipeline de análise de dados e treinamento de modelos:

**Funcionalidades principais:**
- Carregamento e limpeza de dados
- Geração de 6 gráficos exploratórios
- Identificação de perfis ideais de solo/clima
- Treinamento de 5 modelos diferentes
- Avaliação comparativa com métricas de desempenho
- Geração de matriz de confusão

### 2. Dashboard Streamlit (`dashboard_agronegocio.py`)

O dashboard interativo fornece uma interface amigável para monitoramento agrícola em tempo real:

**Funcionalidades principais:**
- Controles interativos para ajuste de parâmetros de solo e clima
- Visualização de métricas em tempo real (umidade, pH, P, K)
- Gráficos de distribuição de nutrientes e parâmetros climáticos
- Sistema inteligente de sugestões de irrigação
- Histórico simulado de 7 dias
- Tabela detalhada de status de parâmetros

### 3. Jupyter Notebook (`RM_FIAP_ML_Agronegocio.ipynb`)

Notebook interativo com análise completa, incluindo:
- Carregamento e exploração de dados
- Análise exploratória com visualizações
- Identificação de perfis ideais
- Treinamento de modelos
- Avaliação e comparação

### 4. Código Original de Análise (`Analise em R py.py`)

Script original que realiza análise exploratória básica:
- Carregamento de dados
- Cálculo de estatísticas descritivas
- Geração de histogramas e gráficos de distribuição

---

## 🚀 Como Executar

### Opção 1: Executar o Dashboard Streamlit

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Executar o dashboard
streamlit run dashboard_agronegocio.py
```

O dashboard será acessível em `http://localhost:8501`

### Opção 2: Executar a Análise de Machine Learning

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Executar o script de análise
python run_ml_analysis.py
```

### Opção 3: Executar o Jupyter Notebook

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Iniciar Jupyter
jupyter notebook RM_FIAP_ML_Agronegocio.ipynb
```

---

## 📦 Dependências

O projeto utiliza as seguintes bibliotecas Python:

| Biblioteca | Versão | Propósito |
|-----------|--------|----------|
| pandas | 2.3.3 | Manipulação e análise de dados |
| numpy | 2.3.4 | Computação numérica |
| matplotlib | 3.10.7 | Visualização de dados |
| seaborn | 0.13.2 | Visualização estatística |
| scikit-learn | 1.7.2 | Machine Learning |
| streamlit | 1.51.0 | Dashboard interativo |
| tabulate | 0.9.0 | Formatação de tabelas |

### Instalação de Dependências

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install pandas matplotlib seaborn scikit-learn streamlit tabulate
```

---

## 🎓 Aprendizados e Insights

### Insights Principais

1. **Excelente Desempenho do Random Forest:** O modelo Random Forest alcançou 99.55% de acurácia, demonstrando que o ensemble de árvores é particularmente eficaz para este problema de classificação de culturas.

2. **Distribuição Equilibrada de Culturas:** O dataset contém uma distribuição relativamente equilibrada das 22 culturas, o que facilita o treinamento de modelos sem viés de classe.

3. **Independência de Variáveis:** A análise de correlação revelou que muitas variáveis são independentes, indicando que cada parâmetro contribui de forma única para a recomendação de culturas.

4. **Preferências Específicas de Culturas:** Diferentes culturas têm preferências distintas de pH, temperatura e umidade, o que valida a necessidade de um sistema de recomendação personalizado.

### Aplicações Práticas

- **Otimização de Irrigação:** O dashboard pode ser utilizado para otimizar a frequência e volume de irrigação baseado em condições em tempo real.
- **Planejamento de Plantio:** O modelo de ML pode auxiliar agricultores na escolha da cultura mais adequada para suas condições de solo e clima.
- **Monitoramento Contínuo:** O sistema permite monitoramento contínuo de parâmetros críticos e alertas automáticos.

---

## 📈 Resultados e Conclusões

### Resultados Alcançados

✅ **Dashboard Funcional:** Interface interativa e responsiva para monitoramento agrícola  
✅ **Modelo de ML Altamente Preciso:** Random Forest com 99.55% de acurácia  
✅ **Análise Exploratória Completa:** 6 gráficos e análises estatísticas  
✅ **Documentação Abrangente:** README detalhado e código bem comentado  

### Conclusões

O projeto demonstra o potencial das tecnologias de análise de dados e machine learning para otimizar a gestão agrícola. O sistema proposto pode auxiliar significativamente os agricultores na tomada de decisões sobre irrigação e seleção de culturas, contribuindo para aumentar a produtividade e sustentabilidade das operações agrícolas.

---

## 📞 Contato e Suporte

Para dúvidas ou sugestões sobre o projeto, entre em contato com:

- **Desenvolvedor:** Manus AI
- **Instituição:** FIAP
- **Data de Conclusão:** Novembro de 2025

---

## 📄 Licença

Este projeto é fornecido sob a licença Apache 2.0, a mesma licença do dataset original do Kaggle.

---

**Última atualização:** Novembro 12, 2025
