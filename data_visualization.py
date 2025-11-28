import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

DB_NAME = 'flexmedia_totem.db'
TABLE_NAME = 'interacoes_totem'
OUTPUT_DIR = 'visualizacoes'

def load_data():
    """Carrega os dados do SQLite para um DataFrame do Pandas."""
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query(f"SELECT * FROM {TABLE_NAME}", conn)
    conn.close()
    return df

def create_visualizations(df):
    """Gera e salva os gráficos de visualização."""
    
    # 1. Limpeza e Preparação dos Dados
    df_cleaned = df.dropna(subset=['interaction_type']).copy()
    df_cleaned['timestamp'] = pd.to_datetime(df_cleaned['timestamp'])
    
    if df_cleaned.empty:
        print("Nenhum dado de interação para visualização.")
        return

    # Cria o diretório de saída
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # --- Gráfico 1: Ativações Diárias ---
    df_cleaned['date'] = df_cleaned['timestamp'].dt.date
    daily_activations = df_cleaned.groupby('date').size()
    
    plt.figure(figsize=(10, 6))
    daily_activations.plot(kind='bar', color='skyblue')
    plt.title('Ativações Diárias do Totem')
    plt.xlabel('Data')
    plt.ylabel('Número de Ativações')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'ativacoes_diarias.png'))
    plt.close()
    print(f"Gráfico 'ativacoes_diarias.png' salvo em '{OUTPUT_DIR}'")

    # --- Gráfico 2: Distribuição do Tipo de Interação ---
    interaction_counts = df_cleaned['interaction_type'].value_counts()
    
    plt.figure(figsize=(8, 8))
    plt.pie(interaction_counts, labels=interaction_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightgreen'])
    plt.title('Distribuição do Tipo de Interação (Curta vs. Longa)')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'distribuicao_interacao.png'))
    plt.close()
    print(f"Gráfico 'distribuicao_interacao.png' salvo em '{OUTPUT_DIR}'")

    # --- Gráfico 3: Duração Média da Interação por Dia (Linha) ---
    daily_avg_duration = df_cleaned.groupby('date')['interaction_duration'].mean()
    
    plt.figure(figsize=(10, 6))
    daily_avg_duration.plot(kind='line', marker='o', color='darkblue')
    plt.title('Duração Média da Interação por Dia')
    plt.xlabel('Data')
    plt.ylabel('Duração Média (segundos)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'duracao_media_diaria.png'))
    plt.close()
    print(f"Gráfico 'duracao_media_diaria.png' salvo em '{OUTPUT_DIR}'")

if __name__ == '__main__':
    # Ativar o ambiente virtual
    # O script será executado via shell com o ambiente ativado
    
    # 1. Carregar os dados
    data_df = load_data()
    
    # 2. Gerar Visualizações
    create_visualizations(data_df)
    
    print("Geração de visualizações concluída.")
