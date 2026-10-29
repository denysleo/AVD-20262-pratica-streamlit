# Justificativa das métricas — Dashboard 2 (Titanic)



## 1. Total de passageiros 

- **Variável(is) utilizada(s):** registros de `df_filtrado`.
- **O que mede:** quantidade de registros que permanecem depois da aplicação dos filtros selecionados.
- **Por que foi escolhida:** fornece contexto para interpretar as demais métricas e deixa claro o tamanho do recorte analisado.
- **Público-alvo:** estudantes, docentes e pessoas que consultam o dashboard.
- **Qual decisão ou interpretação pode apoiar:** ajuda a verificar se uma conclusão está sendo feita com base em muitos ou poucos registros.
- **O que comunica:** volume de passageiros considerados no recorte atual.


## 2. Taxa de sobrevivência

- **Variável(is) utilizada(s):** `sobreviveu`.
- **O que mede:** proporção dos passageiros do recorte classificados como sobreviventes entre os registros com classificação conhecida.
- **Por que foi escolhida:** sobrevivência é um dos resultados centrais do conjunto Titanic e ajuda a resumir a composição do recorte.
- **Público-alvo:** estudantes, docentes e pessoas interessadas em explorar o conjunto de dados.
- **Qual decisão ou interpretação pode apoiar:** permite comparar descritivamente recortes diferentes e formular perguntas para investigação posterior.
- **O que comunica:** percentual de registros classificados como sobreviventes no recorte atual.

## 3. Tarifa média

- **Variável(is) utilizada(s):** `Fare`.
- **O que mede:** média dos valores de tarifa nos registros do recorte atual.
- **Por que foi escolhida:** resume o nível médio das tarifas no grupo analisado e pode motivar comparações descritivas entre grupos.
- **Público-alvo:** estudantes, docentes e pessoas que analisam os dados históricos.
- **Qual decisão ou interpretação pode apoiar:** orienta a investigação de possíveis diferenças de tarifa entre recortes, sempre considerando outras variáveis e limitações do conjunto.
- **O que comunica:** valor médio de `Fare` para os passageiros incluídos.

## 4. Idade média 

- **Variável(is) utilizada(s):** `Age`.
- **O que mede:** média de idade dos passageiros cujo valor de idade está preenchido.
- **Por que foi escolhida:** ajuda a descrever o perfil etário da amostra e a contextualizar as distribuições por idade.
- **Público-alvo:** estudantes, docentes e pessoas que exploram o dataset.
- **Qual decisão ou interpretação pode apoiar:** ajuda a comparar descritivamente recortes etários e a identificar perguntas para a análise exploratória.
- **O que comunica:** idade média dos passageiros com idade conhecida.
