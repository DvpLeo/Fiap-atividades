# Fiap-atividades
Atividade fase 2 cap 1
# Projeto de Sistema de Irrigação Inteligente - FarmTech Solutions (Fase 2)
## Descrição do Projeto
Este projeto avança o sistema de gestão agrícola da FarmTech Solutions, baseado na Fase 1 (cálculo de área plantada e monitoramento climático).
- **Sensores Utilizados**:
  - Nutrientes N, P e K: Simulados por botões verdes (true se pressionado, false se não).
  - pH do solo: Simulado por um LDR (Light Dependent Resistor), com valores de 0 a 14. Se N, P e K estiverem presentes, ajustamos o pH dinamicamente.
  - Umidade do solo: Simulada por um DHT22 (medidor de umidade do ar, usado como proxy).
- **Objetivo**: Monitorar em tempo real e decidir se liga um relé (simulando uma bomba d'água) com base nos dados coletados.

## Funcionamento do Sistema
O sistema é simulado em Python. lógica principal:
- **Simulação de Sensores**:
  - Os botões para N, P e K são verificados como booleanos. Se alterados, afetam o pH (ex.: se todos pressionados, aumenta o pH).
  - O LDR simula pH analógico, variando de 0 a 14, com referência a 7 como neutro.
  - O DHT22 simula umidade, e se for abaixo de 50%, considera-se irrigação necessária.
- **Lógica de Decisão**:
  - Para a cultura de tomate (escolhida como exemplo), irrigamos se:
    - Umidade < 50%.
    - pH entre 6 e 7.
    - N, P e K presentes (botões pressionados).
  - Integração com API OpenWeather: Se a previsão for 'rain', suspende a irrigação para economizar recursos.
  - Exemplo de fluxo: No código, um loop verifica os sensores a cada 5 segundos e imprime a decisão.
