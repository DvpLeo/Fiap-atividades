# Leonardo_Pietro_RM568219_fase2_cap9
import pandas as pd  # Para manipulação de dados
import matplotlib.pyplot as plt  # Para gráficos
from matplotlib import style  # Estilo para usabilidade
import os  # Para verificar arquivos

# Passo 1: Carregar a base de dados
try:
    dados = pd.read_excel("dados_agro.xlsx")  # Substitua pelo caminho do seu arquivo
    print("Dados carregados com sucesso.")
except FileNotFoundError:
    print("Erro: Arquivo dados_agro.xlsx não encontrado.")
    exit()
except Exception as e:
    print(f"Erro ao carregar dados: {e}")
    exit()

# Validação de dados: Garantir que as colunas existam
if not all(col in dados.columns for col in ['Tonelagens', 'Tipo_Cultura']):
    print("Erro: Colunas obrigatórias ausentes.")
    exit()

dados = dados.dropna(subset=['Tonelagens', 'Tipo_Cultura'])  # Limpeza inicial

# Passo 2: Análise exploratória de variável quantitativa (Tonelagens)
tonelagens = dados['Tonelagens']

# Medidas de Tendência Central
media = tonelagens.mean()
mediana = tonelagens.median()
moda = tonelagens.mode()[0]  # Primeira moda

# Medidas de Dispersão
variancia = tonelagens.var()
desvio_padrao = tonelagens.std()

# Medidas Separatrizes
quartis = tonelagens.quantile([0.25, 0.5, 0.75])
minimo = tonelagens.min()
maximo = tonelagens.max()

# Impressão limpa e objetiva
print("\nAnálise Exploratória de Tonelagens:")
print(f"  - Média: {media:.2f}")
print(f"  - Mediana: {mediana:.2f}")
print(f"  - Moda: {moda:.2f}")
print(f"  - Variância: {variancia:.2f}")
print(f"  - Desvio Padrão: {desvio_padrao:.2f}")
print(f"  - Quartis: {quartis.to_dict()}")
print(f"  - Mínimo: {minimo:.2f}")
print(f"  - Máximo: {maximo:.2f}")

# Análise Gráfica para variável quantitativa
plt.figure(figsize=(8, 6))
plt.hist(tonelagens, bins=10, edgecolor='black', color='blue')
plt.title("Histograma de Tonelagens")
plt.xlabel("Tonelagens")
plt.ylabel("Frequência")
plt.grid(True)
plt.savefig("histograma_tonelagens.png")  # Salva para usabilidade
plt.show()

# Passo 3: Análise de variável qualitativa (Tipo_Cultura)
# Gráfico para variável qualitativa
tipo_cultura_counts = dados['Tipo_Cultura'].value_counts()
plt.figure(figsize=(8, 6))
tipo_cultura_counts.plot(kind='bar', color='green', edgecolor='black')
plt.title("Distribuição de Tipo de Cultura")
plt.xlabel("Tipo de Cultura")
plt.ylabel("Contagem")
plt.grid(axis='y')
plt.savefig("grafico_tipo_cultura.png")
plt.show()

print("Análises concluídas com sucesso.")
