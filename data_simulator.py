import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Nome do banco de dados
DB_NAME = 'flexmedia_totem.db'
TABLE_NAME = 'interacoes_totem'
NUM_RECORDS = 500

def create_database_and_table():
    """Cria o banco de dados SQLite e a tabela de interações."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            pir_sensor INTEGER NOT NULL,
            touch_sensor INTEGER NOT NULL,
            interaction_duration REAL,
            interaction_type TEXT
        );
    """)
    conn.commit()
    conn.close()
    print(f"Banco de dados '{DB_NAME}' e tabela '{TABLE_NAME}' criados com sucesso.")

def generate_simulated_data(num_records):
    """Gera dados simulados de interações do totem."""
    start_time = datetime.now() - timedelta(days=7)
    
    data = {
        'timestamp': [],
        'pir_sensor': [],
        'touch_sensor': [],
        'interaction_duration': [],
        'interaction_type': []
    }

    for i in range(num_records):
        # Simula o tempo
        current_time = start_time + timedelta(minutes=i * 10)
        data['timestamp'].append(current_time.strftime('%Y-%m-%d %H:%M:%S'))
        
        # Simula o sensor PIR (presença) - 80% de chance de ter presença
        pir = np.random.choice([1, 0], p=[0.8, 0.2])
        data['pir_sensor'].append(pir)
        
        # Simula o sensor de toque - 60% de chance de toque se houver presença
        if pir == 1:
            touch = np.random.choice([1, 0], p=[0.6, 0.4])
        else:
            touch = 0
        data['touch_sensor'].append(touch)
        
        # Simula a duração da interação se houver toque
        if touch == 1:
            # Duração entre 0.1 e 5.0 segundos
            duration = np.random.uniform(0.1, 5.0)
            data['interaction_duration'].append(round(duration, 2))
            
            # Classificação simples para ML: 'short' (< 1.5s) ou 'long' (>= 1.5s)
            if duration < 1.5:
                data['interaction_type'].append('short')
            else:
                data['interaction_type'].append('long')
        else:
            data['interaction_duration'].append(None)
            data['interaction_type'].append(None)

    return pd.DataFrame(data)

def insert_data_to_db(df):
    """Insere o DataFrame no banco de dados SQLite."""
    conn = sqlite3.connect(DB_NAME)
    
    # Usando o método to_sql do pandas para inserção eficiente
    df.to_sql(TABLE_NAME, conn, if_exists='replace', index=False)
    
    conn.close()
    print(f"Dados simulados ({len(df)} registros) inseridos na tabela '{TABLE_NAME}'.")

if __name__ == '__main__':
    # 1. Cria o banco de dados e a tabela
    create_database_and_table()
    
    # 2. Gera os dados simulados
    simulated_df = generate_simulated_data(NUM_RECORDS)
    
    # 3. Insere os dados no banco de dados
    insert_data_to_db(simulated_df)
    
    print("Simulação de dados e armazenamento concluída.")
