# Challenge FlexMedia - Totem Inteligente (Entrega 2)

Este repositório contém a solução proposta para a segunda entrega do Challenge FlexMedia, focada na integração de sensores simulados, persistência de dados em SQL, análise estatística, aplicação de Machine Learning e visualização de métricas de uso.

## Descrição Técnica do Sistema e Módulos

O projeto simula o fluxo de dados do **Totem Inteligente FlexMedia**, conforme a arquitetura proposta.

### Módulos do Projeto

| Arquivo | Função | Requisito Atendido |
| :--- | :--- | :--- |
| `data_simulator.py` | Simula a coleta de dados de sensores (PIR e Toque) e armazena em `flexmedia_totem.db` (SQLite). | Demonstração da integração entre sensores e banco de dados SQL. |
| `data_analysis_ml.py` | Carrega os dados do SQL, realiza limpeza, análise estatística e treina um modelo de Machine Learning (Árvore de Decisão) para classificar o tipo de interação. | Aplicação de conceitos de modelagem de dados e Machine Learning supervisionado. |
| `data_visualization.py` | Gera gráficos de visualização (dashboard simples) a partir dos dados analisados. | Criação de visualizações iniciais em forma de dashboard front-end simples com Python. |
| `flexmedia_totem.db` | Banco de dados SQLite contendo os dados simulados de interação. | Armazenamento SQL. |
| `interaction_classifier.joblib` | Modelo de Machine Learning treinado e serializado. | Modelo de ML. |
| `DOCUMENTACAO_TECNICA.md` | Documentação detalhada da arquitetura, fluxo de dados e prints de execução. | Documentação Técnica. |
| `setup_repo.py.py` | Arquivo XML do Diagrama de Arquitetura (fornecido). | Diagramas e visualizações gerados. |

## Fluxo de Dados e Conexões

O fluxo de dados representa a jornada da informação no totem:

**Coleta (Sensor Simulado)** → **Armazenamento (SQLite)** → **Análise (Python/Pandas)** → **ML (Scikit-learn)** → **Visualização (Matplotlib)**

1.  **Geração de Dados**: `data_simulator.py` gera dados de `pir_sensor`, `touch_sensor` e `interaction_duration`.
2.  **Persistência**: Os dados são escritos no `flexmedia_totem.db`.
3.  **Processamento**: `data_analysis_ml.py` lê o banco, limpa os dados (removendo interações nulas), calcula métricas e treina o modelo de ML.
4.  **Visualização**: `data_visualization.py` gera gráficos de métricas de uso, salvos em `visualizacoes/`.

## Requisitos de Execução

Para executar o projeto, é necessário ter Python 3.x e as seguintes bibliotecas instaladas (o ambiente virtual `venv` foi utilizado na simulação):

```bash
pip install pandas scikit-learn matplotlib sqlalchemy
```

## Scripts de Demonstração

Para recriar o ambiente e executar a simulação:

1.  **Simular Dados e Criar DB:**
    ```bash
    python3 data_simulator.py
    ```
2.  **Analisar Dados e Treinar ML:**
    ```bash
    python3 data_analysis_ml.py
    ```
3.  **Gerar Visualizações:**
    ```bash
    python3 data_visualization.py
    ```

## Entregáveis

Todos os arquivos gerados, incluindo os scripts Python, o banco de dados (`flexmedia_totem.db`), o modelo de ML (`interaction_classifier.joblib`), os gráficos (`visualizacoes/`) e a documentação (`DOCUMENTACAO_TECNICA.md`), compõem os entregáveis do projeto.

---
*Desenvolvido por Manus AI para o Challenge FlexMedia.*
