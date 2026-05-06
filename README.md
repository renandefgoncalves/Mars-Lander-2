# Mars Lander - Episódio 2

## O Objetivo
O objetivo deste projeto é desenvolver um programa capaz de pousar com segurança a nave "Mars Lander" em uma área específica da superfície de Marte. A nave transporta o rover Opportunity e é controlada por um algoritmo que deve ajustar o ângulo de inclinação e a potência dos propulsores para garantir a integridade da missão.

## Regras e Ambiente
O simulador situa a nave em uma zona do céu marciano com **7000m** de largura e **3000m** de altura.

<img width="468" height="265" alt="Ambiente de Marte" src="https://github.com/user-attachments/assets/0bf2d10a-1e3a-45d7-b7a3-2bb82e6b1b5d" />

* **Terreno:** Existe apenas uma **área de solo plano** na superfície, com pelo menos **1000m** de largura.
* **Controles:** O programa deve fornecer o ângulo de inclinação (**-90° a 90°**) e a potência de empuxo (**0 a 4**) a cada segundo.
* **Física:** A gravidade em Marte é de **3,711 m/s²**. Uma potência de empuxo de 4 compensa a gravidade em uma posição vertical.
* **Consumo:** Para cada unidade de potência $X$, são consumidos $X$ litros de combustível por segundo.

<img width="505" height="208" alt="Controles da Nave" src="https://github.com/user-attachments/assets/be82258f-453b-4292-8190-3656e94a1760" />

### Requisitos para um Pouso Bem-Sucedido
Para não destruir a nave, os seguintes parâmetros devem ser respeitados no momento do contacto com o solo:
1.  Pousar exactamente sobre o **solo plano**.
2.  Estar em **posição vertical** (ângulo de inclinação = 0°).
3.  **Velocidade vertical** limitada a ≤ 40 m/s (em valor absoluto).
4.  **Velocidade horizontal** limitada a ≤ 20 m/s (em valor absoluto).

## Estrutura do Projecto

* **Linguagem:** Python 3
* **Entrada:** Dados de inicialização da superfície e dados de telemetria em tempo real (X, Y, velocidades, combustível, etc.).
* **Saída:** Comando de rotação e potência por turno.

### Restrições Técnicas
* O ângulo pode mudar no máximo **15°** por turno.
* A potência pode mudar no máximo **1** unidade por turno.
* Tempo de resposta máximo de **100ms** por turno.

---

## Insights de Desenvolvimento

1.  **Código Unificado:** O algoritmo foi desenvolvido para ser robusto o suficiente para passar nos 5 testes do simulador sem ajustes manuais, lidando com diferentes coordenadas e velocidades iniciais.
2.  **Lógica de Estados:** Em vez de usar frames fixos ou tempos pré-determinados, o código utiliza lógica baseada na distância até o alvo e controlo de velocidade vetorial.
3.  **Ganho de Altitude:** A nave possui capacidade de subir se necessário (usando potência 4 e ângulo vertical), permitindo desviar de obstáculos antes de atingir a zona de pouso.

## Como Executar

1.  Copie o código contido no ficheiro `app.py` deste repositório.
2.  Aceda ao desafio no [CodinGame - Mars Lander Episode 2](https://www.codingame.com/ide/puzzle/mars-lander-episode-2).
3.  Cole o código no editor da plataforma.
4.  Selecione **Python 3** como linguagem.
5.  Clique em **Play All Test Cases** para validar a solução.

---
*Este projecto foi desenvolvido como parte de um estudo de lógica de programação e automação com Python.*
