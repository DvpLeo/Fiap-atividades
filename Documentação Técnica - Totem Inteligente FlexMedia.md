# Documentação Técnica - Totem Inteligente FlexMedia

## 1. Introdução

Este documento detalha a implementação da solução proposta para o **Challenge FlexMedia**, focada na segunda entrega do desafio. O objetivo é demonstrar a integração funcional entre a simulação de sensores, o armazenamento de dados em um banco de dados SQL (SQLite), a limpeza e análise estatística dos dados, e a aplicação de um modelo de Machine Learning supervisionado simples, culminando na visualização de métricas de uso.

## 2. Arquitetura Implementada

A arquitetura implementada simula o fluxo de dados do Totem Inteligente FlexMedia, conforme o diagrama de arquitetura fornecido. A solução foi desenvolvida em Python, utilizando bibliotecas como `pandas`, `sqlite3`, `matplotlib` e `scikit-learn`.

### 2.1. Diagrama de Arquitetura

O diagrama a seguir ilustra a arquitetura conceitual do sistema, com foco na jornada do dado, desde a interação do usuário até a análise na nuvem (simulada localmente):

*(O diagrama original em XML foi fornecido no arquivo `setup_repo.py.py` e deve ser visualizado separadamente. A simulação atual foca nos módulos locais e na persistência de dados.)*

**Módulos Simulados e Tecnologias:**

| Módulo Conceitual | Módulo Implementado (Simulação) | Tecnologia Principal | Função |
| :--- | :--- | :--- | :--- |
| **Sensores** (Touch, PIR) | `data_simulator.py` | Python (`numpy`) | Geração de dados de presença (`pir_sensor`) e toque (`touch_sensor`) com duração de interação. |
| **ESP32 / ESP32-CAM** | `data_simulator.py` | Python (`sqlite3`) | Coleta, estruturação e envio dos dados simulados para o banco de dados. |
| **AWS IoT Core / AWS Lambda** | `data_analysis_ml.py` | Python (`pandas`, `sqlite3`) | Leitura dos dados persistidos, limpeza, análise estatística e treinamento do modelo de ML. |
| **Amazon S3 / QuickSight** | `data_visualization.py` | Python (`matplotlib`) | Geração de gráficos de visualização de métricas de uso. |

## 3. Fluxo de Dados (Entrada → Processamento → Saída)

O fluxo de dados da simulação segue as seguintes etapas:

1.  **Entrada (Simulação de Sensores)**:
    *   O script `data_simulator.py` gera 500 registros simulados de interações ao longo de 7 dias.
    *   Os dados incluem `timestamp`, estado do sensor PIR (presença), estado do sensor de toque, `interaction_duration` (duração em segundos) e `interaction_type` (classificação 'short' ou 'long').

2.  **Armazenamento (Persistência SQL)**:
    *   O `data_simulator.py` cria o banco de dados SQLite (`flexmedia_totem.db`) e a tabela `interacoes_totem`.
    *   Os dados simulados são inseridos na tabela, simulando a persistência de dados brutos do dispositivo.

3.  **Processamento (Limpeza e Análise)**:
    *   O script `data_analysis_ml.py` carrega os dados do SQLite.
    *   **Limpeza**: Registros sem interação (`interaction_type` nulo) são removidos.
    *   **Análise Estatística**: Cálculo de métricas como o total de ativações e a duração média da interação.

4.  **Processamento (Machine Learning)**:
    *   O `data_analysis_ml.py` treina um modelo de **Árvore de Decisão** (`DecisionTreeClassifier`) para classificar o `interaction_type` ('short' ou 'long') com base na `interaction_duration`.
    *   O modelo é salvo no arquivo `interaction_classifier.joblib` para uso futuro.

5.  **Saída (Visualização)**:
    *   O script `data_visualization.py` lê os dados limpos e gera três gráficos principais:
        *   Ativações Diárias (Barra)
        *   Distribuição do Tipo de Interação (Pizza)
        *   Duração Média da Interação por Dia (Linha)
    *   Os gráficos são salvos como imagens PNG no diretório `visualizacoes/`.

## 4. Prints de Execução e Dashboards

### 4.1. Execução da Análise e ML

A execução do script de análise e ML demonstra a limpeza dos dados, as métricas estatísticas e a alta acurácia do modelo de classificação (1.00), indicando que a duração da interação é um preditor perfeito para o tipo de interação na simulação.

\`\`\`
--- Análise e Limpeza de Dados ---
Registros originais: 500
Registros com interação (limpos): 258
--- Métricas de Uso ---
Total de Ativações Registradas: 258
Duração Média da Interação: 2.47 segundos
--- Distribuição do Tipo de Interação ---
interaction_type
long     175
short     83
Name: count, dtype: int64

--- Treinamento do Modelo de Machine Learning ---
Acurácia do Modelo: 1.00
Relatório de Classificação:
              precision    recall  f1-score   support

        long       1.00      1.00      1.00        48
       short       1.00      1.00      1.00        30

    accuracy                           1.00        78
   macro avg       1.00      1.00      1.00        78
weighted avg       1.00      1.00      1.00        78

Modelo salvo em 'interaction_classifier.joblib'
\`\`\`

