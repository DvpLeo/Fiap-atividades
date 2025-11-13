# Projeto: Dashboard e Machine Learning para Agronegócio

## Objetivo
Organizar o repositório, documentar o processo e fornecer instruções para reprodução. Este repositório foi criado automaticamente a partir do conjunto de arquivos fornecido pelo usuário.

## Estrutura do repositório
```
/ (raiz)
├─ data/                  # Dados brutos (Excel, SQL exemplo)
├─ notebooks/             # Notebooks Jupyter (.ipynb)
├─ src/                   # Scripts Python executáveis (.py)
├─ docs/                  # Documentação e arquivos RTF/MD
├─ images/                # Gráficos e screenshots
├─ .github/               # (opcional) workflows e templates
README.md
requirements.txt
```
## Conteúdo notável
- `notebooks/RM_FIAP_ML_Agronegocio.ipynb` - Notebook principal com análises exploratórias e modelos.
- `src/run_ml_analysis.py` - Script para executar análise/modelo.
- `src/dashboard_agronegocio.py` - Script de dashboard (streamlit/plotly dependendo do conteúdo).
- `data/Book2(1).xlsx` - Planilha fornecida.
- `images/1_distribuicao_culturas.png`, `2_distribuicao_nutrientes.png`, ... - Gráficos gerados no projeto.
- `data/select_all_example.sql` - Arquivo de exemplo com `SELECT *` para uso no Oracle SQL Developer.

## Documentação (README.md) — requisitos solicitados
Você pediu especificamente que o README incluísse:
1. **Explicação detalhada do processo** — descrita na seção "Processo" abaixo.  
2. **Prints de tela das etapas no Oracle SQL Developer** — incluí um placeholder (`images/oracle_screenshot_placeholder.png`). Substitua por screenshots reais do seu ambiente:  
   - Abra o Oracle SQL Developer, conecte ao banco, navegue até a tabela alvo.  
   - Execute a query `SELECT * FROM SCHEMA.TABLE;` (substitua SCHEMA.TABLE).  
   - Faça capturas de tela das etapas (conexão, query, resultados) e salve-as em `images/` com nomes como `oracle_conn.png`, `oracle_query.png`, `oracle_result.png`.
3. **Consulta SELECT \*** — forneci `data/select_all_example.sql` como exemplo. Inclua no README abaixo o resultado da execução (copie e cole a saída ou um screenshot).

## Processo (passo-a-passo)
1. **Reproduzir ambiente Python**  
   - Crie e ative um ambiente virtual:  
     ```bash
     python -m venv .venv
     source .venv/bin/activate   # Linux/macOS
     .venv\Scripts\activate    # Windows PowerShell/CMD
     ```
   - Instale dependências (exemplo):  
     ```bash
     pip install -r requirements.txt
     ```
2. **Exploração de dados**  
   - Abra `notebooks/RM_FIAP_ML_Agronegocio.ipynb` no Jupyter Lab/Notebook e siga as células.  
   - Ou rode `python src/run_ml_analysis.py` para executar o pipeline automatizado (se o script estiver pronto).  
3. **Execução de queries no Oracle SQL Developer**  
   - Conecte ao banco, abra um worksheet, cole `data/select_all_example.sql` e execute.  
   - Salve screenshots em `images/` para documentação.
4. **Resultados e visualizações**  
   - Os gráficos já fornecidos estão em `images/` (1_.. a 6_..). Inclua explicações dos gráficos no README ou no notebook conforme necessário.
5. **Publicar no GitHub**  
   - Inicie repositório: `git init`, adicione `.gitignore`, commit e publique no GitHub com `git remote add origin ...` e `git push -u origin main`.

## Exemplo de seção que você deve completar manualmente (para nota)
### Prints do Oracle SQL Developer
- `images/oracle_conn.png` - (adicione sua captura)
- `images/oracle_query.png` - (adicione sua captura)
- `images/oracle_result.png` - (adicione sua captura)

### Output da query `SELECT *`
Cole aqui o resultado (ou adicione `images/oracle_result.png` como screenshot).

## Requisitos e execução automática
Criei um `requirements.txt` mínimo baseado em dependências comuns para análise e dashboard.
