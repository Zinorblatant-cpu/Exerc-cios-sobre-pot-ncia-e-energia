# Cálculo de Potências em Motores Elétricos

Este documento apresenta os cálculos de potência para quatro motores elétricos distintos, detalhando as potências útil, ativa, aparente e reativa. Esses cálculos são essenciais para compreender o desempenho dos motores e garantir uma operação eficiente.

## Conteúdo do Documento

### Motor 1
- **Potência Útil (Pnu):** 130 W  
- **Rendimento (η):** 0,50  
- **Fator de Potência (cosφ):** 0,58  

#### Cálculos:
- **Potência Ativa (Pa):**
  ```math
  Pa = \frac{Pnu}{\eta} = \frac{130}{0,50} = 260W
  ```
- **Potência Aparente (S):**
  ```math
  S = \frac{Pa}{cosφ} = \frac{260}{0,58} = 448VA
  ```
- **Potência Reativa (Q):**
  ```math
  Q = \sqrt{S^2 - Pa^2} = \sqrt{448^2 - 260^2} = 365VAr
  ```

### Motor 2
- **Potência Útil (Pnu):** 75.000 W  
- **Rendimento (η):** 0,946  
- **Fator de Potência (cosφ):** 0,85  

#### Cálculos:
- **Potência Ativa (Pa):**
  ```math
  Pa = \frac{Pnu}{\eta} = \frac{75000}{0,946} = 79.281W
  ```
- **Potência Aparente (S):**
  ```math
  S = \frac{Pa}{cosφ} = \frac{79281}{0,85} = 93.271VA
  ```
- **Potência Reativa (Q):**
  ```math
  Q = \sqrt{S^2 - Pa^2} = \sqrt{93271^2 - 79281^2} = 49.134VAr
  ```

### Motor 3
- **Potência Útil (Pnu):** 300.000 W  
- **Rendimento (η):** 0,958  
- **Fator de Potência (cosφ):** 0,89  

#### Cálculos:
- **Potência Ativa (Pa):**
  ```math
  Pa = \frac{Pnu}{\eta} = \frac{300000}{0,958} = 313.152W
  ```
- **Potência Aparente (S):**
  ```math
  S = \frac{Pa}{cosφ} = \frac{313152}{0,89} = 351.856VA
  ```
- **Potência Reativa (Q):**
  ```math
  Q = \sqrt{S^2 - Pa^2} = \sqrt{351856^2 - 313152^2} = 160.432VAr
  ```

### Motor 4
- **Potência Útil (Pnu):** 1.100 W  
- **Rendimento (η):** 0,815  
- **Fator de Potência (cosφ):** 0,75  

#### Cálculos:
- **Potência Ativa (Pa):**
  ```math
  Pa = \frac{Pnu}{\eta} = \frac{1100}{0,815} = 1.349W
  ```
- **Potência Aparente (S):**
  ```math
  S = \frac{Pa}{cosφ} = \frac{1349}{0,75} = 1.799VA
  ```
- **Potência Reativa (Q):**
  ```math
  Q = \sqrt{S^2 - Pa^2} = \sqrt{1799^2 - 1349^2} = 1.190VAr
  ```

## Observações

- **Potência Ativa (Pa):** Representa a energia efetivamente convertida em trabalho útil pelo motor.
- **Potência Aparente (S):** Combinação vetorial das potências ativa e reativa.
- **Potência Reativa (Q):** Energia que não realiza trabalho útil, mas é necessária para a operação de equipamentos indutivos ou capacitivos.

## Conclusão

Os cálculos apresentados permitem uma análise detalhada do desempenho energético de cada motor. Com esses resultados, é possível identificar oportunidades para otimizar a eficiência energética, como correção do fator de potência e melhoria do rendimento dos motores.

Caso precise de mais detalhes ou explicações adicionais, consulte as fórmulas utilizadas ou entre em contato com o autor deste documento.
