import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

DB_NAME = 'flexmedia_totem.db'
TABLE_NAME = 'interacoes_totem'
MODEL_FILENAME = 'interaction_classifier.joblib'

def load_data():
    """Carrega os dados do SQLite para um DataFrame do Pandas."""
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query(f"SELECT * FROM {TABLE_NAME}", conn)
    conn.close()
    return df

def data_cleaning_and_analysis(df):
    """Realiza a limpeza, estruturação e análise estatística inicial dos dados."""
    print("--- Análise e Limpeza de Dados ---")
    
    # 1. Limpeza de Dados: Remover registros sem interação (interaction_type é None)
    df_cleaned = df.dropna(subset=['interaction_type']).copy()
    print(f"Registros originais: {len(df)}")
    print(f"Registros com interação (limpos): {len(df_cleaned)}")
    
    # 2. Estruturação: Converter timestamp para datetime
    df_cleaned['timestamp'] = pd.to_datetime(df_cleaned['timestamp'])
    
    # 3. Análise Estatística Inicial
    total_activations = len(df_cleaned)
    avg_duration = df_cleaned['interaction_duration'].mean()
    
    print("\n--- Métricas de Uso ---")
    print(f"Total de Ativações Registradas: {total_activations}")
    print(f"Duração Média da Interação: {avg_duration:.2f} segundos")
    
    # Contagem de tipos de interação
    interaction_counts = df_cleaned['interaction_type'].value_counts()
    print("\n--- Distribuição do Tipo de Interação ---")
    print(interaction_counts)
    
    return df_cleaned

def train_machine_learning_model(df):
    """Treina um modelo de Machine Learning supervisionado simples."""
    print("\n--- Treinamento do Modelo de Machine Learning ---")
    
    # Variáveis preditoras (Features) e Variável Alvo (Target)
    # Usaremos a duração da interação para prever o tipo de interação (short/long)
    # Embora a simulação já defina isso, o objetivo é demonstrar a aplicação de ML.
    X = df[['interaction_duration']]
    y = df['interaction_type']
    
    # Divisão em conjuntos de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Treinamento do modelo (Árvore de Decisão)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Previsão e Avaliação
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Acurácia do Modelo: {accuracy:.2f}")
    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred))
    
    # Salvar o modelo treinado
    joblib.dump(model, MODEL_FILENAME)
    print(f"\nModelo salvo em '{MODEL_FILENAME}'")
    
    return model

if __name__ == '__main__':
    # Ativar o ambiente virtual
    # O script será executado via shell com o ambiente ativado
    
    # 1. Carregar os dados
    data_df = load_data()
    
    # 2. Limpeza e Análise
    cleaned_df = data_cleaning_and_analysis(data_df)
    
    # 3. Treinamento do Modelo de ML
    if not cleaned_df.empty:
        train_machine_learning_model(cleaned_df)
    else:
        print("Não há dados de interação para treinar o modelo.")
