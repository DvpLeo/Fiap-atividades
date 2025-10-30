# 📌 Sprint 1 – Proposta Técnica: Totem Inteligente FlexMedia

> **Repositório privado – Challenge FlexMedia | FIAP**  
> *Documento entregue na Sprint 1 conforme requisitos do enunciado.*

---

## 1. Justificativa do Problema e Descrição da Solução Proposta

### Problema
Espaços culturais, comerciais e de lazer carecem de soluções interativas que promovam engajamento real, personalizem a experiência do visitante e gerem insights úteis sem comprometer a privacidade. Muitos totens atuais são estáticos, genéricos ou coletam dados de forma invasiva.

### Solução Proposta
Desenvolveremos um **Totem Inteligente com IA**, um dispositivo físico integrado a sensores, interface intuitiva e backend em nuvem, capaz de:
- Detectar presença e perfil aproximado do usuário (ex.: faixa etária estimada, nível de interesse);
- Oferecer conteúdos dinâmicos e personalizados (roteiros, promoções, curiosidades);
- Coletar métricas anônimas de engajamento (tempo, interações, preferências);
- Enviar dados para análise em tempo real via nuvem;
- Respeitar rigorosamente a privacidade (LGPD/GDPR by design).

A solução será **multimodal** (toque, voz opcional, sensores) e **multissensorial** (feedback visual, sonoro e háptico leve), ideal para museus, shoppings e centros culturais.

---

## 2. Definição das Tecnologias Utilizadas

### Hardware
- **Microcontrolador**: ESP32 (com Wi-Fi/Bluetooth) ou ESP32-CAM (para visão computacional leve);
- **Sensores**:
  - PIR (detecção de presença);
  - Touch screen capacitivo (7–10”);
  - Sensor de luminosidade (BH1750);
  - Microfone MEMS (opcional, para comandos de voz offline);
- **Atuadores**: Alto-falante pequeno, LED RGB (feedback ambiental).

### Software & IA
- **Linguagens**:
  - C++ (firmware do ESP32);
  - Python (backend, treinamento e inferência de modelos);
  - JavaScript/React (interface gráfica no totem via WebView ou Electron).
- **Bibliotecas/Frameworks**:
  - TensorFlow Lite (modelos de ML leves para classificação de perfil);
  - OpenCV (pré-processamento de imagem local, sem armazenamento);
  - scikit-learn (análise de padrões de uso);
  - Picovoice ou Whisper.cpp (reconhecimento de fala offline).
- **IA pronta de mercado** (opcional e com anonimização):
  - AWS Rekognition ou Azure Computer Vision (apenas para inferência em tempo real, sem persistência de imagens).

### Serviços em Nuvem
- **Plataforma**: AWS (escolhida por suporte acadêmico e robustez em IoT);
- **Serviços**:
  - AWS IoT Core → comunicação segura com dispositivos;
  - AWS Lambda → processamento serverless de dados;
  - Amazon S3 → armazenamento de métricas agregadas;
  - Amazon QuickSight → dashboard de analytics para clientes da FlexMedia;
  - Amazon Cognito → autenticação segura para administradores.

---

## 3. Esboço da Arquitetura da Solução

> **Diagrama de arquitetura**: disponível em `docs/architecture.drawio`  


### Visão Geral (Pipeline de Dados)
1. **Camada de Interação (Edge)**:
   - Usuário interage com totem (toque, voz, aproximação).
   - Sensores capturam sinais anônimos.
2. **Camada de Processamento Local**:
   - ESP32 executa lógica de detecção e roteamento.
   - Modelo de IA leve (TensorFlow Lite) classifica perfil.
3. **Camada de Comunicação**:
   - Dados criptografados enviados via MQTT/HTTPS para AWS IoT Core.
4. **Camada de Nuvem**:
   - Lambda processa e enriquece os dados.
   - Métricas salvas no S3 e visualizadas no QuickSight.
5. **Feedback Loop**:
   - Conteúdos atualizados dinamicamente com base em insights coletivos.

---

## 4. Estratégia de Coleta de Dados

### Dados Coletados (todos anônimos)
- Tempo médio de interação por sessão;
- Número de toques e caminhos percorridos na interface;
- Tipo de conteúdo selecionado (ex.: “história”, “promoção”, “mapa”);
- Estimativa não identificável de faixa etária/gênero (via visão computacional **sem salvar imagens**);
- Contagem de visitantes por faixa horária.

### Dados **NÃO** Coletados
- Nome, e-mail, CPF, rosto, localização GPS, identificadores únicos persistentes.

### Consentimento e Transparência
- Tela inicial com mensagem clara:  
  _“Este totem coleta dados anônimos para melhorar sua experiência. Ao continuar, você concorda com nossa política de privacidade.”_
- Botão “Modo Privado”: desativa coleta, mantém funcionalidades básicas.

### Armazenamento
- Dados brutos: mantidos por **7 dias** (depuração);
- Métricas agregadas: retidas por até **24 meses**;
- Todos os dados em repouso são criptografados (AES-256).

