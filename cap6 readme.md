# Fiap-atividades
Atividade fase 2 cap 6
# Projeto de Otimização Agrícola para Cana-de-Açúcar - FarmTech Solutions

## Introdução
Este projeto aborda o agronegócio, especificamente a redução de perdas na colheita de cana-de-açúcar no Brasil, um setor que gera milhões de empregos e impulsiona a economia. Como parte da Fase 2 da FarmTech Solutions, desenvolvimos uma solução em Python para simular e otimizar a irrigação, integrando tecnologias como sensores simulados e previsão de clima. O foco é na inovação para sustentabilidade, usando conceitos de Python (subalgoritmos, estruturas de dados, arquivos e banco de dados Oracle).

O agronegócio, como definido, envolve a produção e comercialização de produtos agrícolas, com impactos na supply chain e no desenvolvimento humano. Aqui, tratamos das perdas na colheita de cana (até 15% com métodos mecânicos), propondo uma ferramenta que monitora sensores e decide irrigação automaticamente, reduzindo desperdícios.

## Linha Lógica Clara e Objetiva
O desenvolvimento segue uma sequência lógica:
1. **Simulação de Sensores**: Coleta dados de N, P, K, pH e umidade.
2. **Validação de Entradas**: Garante que dados sejam consistentes (ex.: números válidos).
3. **Processamento e Decisão**: Usa subalgoritmos para analisar dados e integrar API para previsão de clima.
4. **Armazenamento e Saída**: Grava em arquivos JSON e banco de dados, apresentando resultados limpos via console.
5. **Inovação**: Integração com Oracle para relatórios históricos, promovendo análise em tempo real.

## Relevância com o Agronegócio
Este projeto foca no agronegócio brasileiro, particularmente na cana-de-açúcar, onde perdas na colheita impactam a produtividade. Inovamos ao usar tecnologia para otimizar processos, alinhando-se aos cinco setores do agronegócio (insumos, produção, processamento, distribuição e serviços). A solução aborda a "AgroTech", oferecendo ferramentas para monitoramento, reduzindo emissões de GEE e melhorando a segurança alimentar.

## Funcionamento do Código
O código, com validação de entradas e saídas limpas:
- **Simulação**: Usa dicionários para estruturas de dados.
- **Validação**: Verifica tipos de entrada para evitar erros.
- **Apresentação de Dados**: Saídas formatadas para usabilidade, ex.:
Ciclo de Simulação:

Sensores: N=True, P=False, K=True, pH=6.5, Umidade=45%
Decisão: Irrigando: Condições ideais!

