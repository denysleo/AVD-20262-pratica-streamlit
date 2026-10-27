# Justificativa das métricas — Dashboard 2 (Titanic)

> Antes da entrega final, confira se a coluna `sobreviveu` contém os rótulos esperados e se estes cálculos correspondem ao DataFrame usado pelo aplicativo. As métricas abaixo são propostas para análise exploratória, não para inferir causalidade.

## 1. Total de passageiros no recorte

- **Variável(is) utilizada(s):** registros de `df_filtrado`.
- **O que mede:** quantidade de registros que permanecem depois da aplicação dos filtros selecionados.
- **Por que foi escolhida:** fornece contexto para interpretar as demais métricas e deixa claro o tamanho do recorte analisado.
- **Público-alvo:** estudantes, docentes e pessoas que consultam o dashboard.
- **Qual decisão ou interpretação pode apoiar:** ajuda a verificar se uma conclusão está sendo feita com base em muitos ou poucos registros.
- **O que comunica:** volume de passageiros considerados no recorte atual.
- **Cálculo sugerido:** `len(df_filtrado)`.

## 2. Taxa de sobrevivência

- **Variável(is) utilizada(s):** `sobreviveu`.
- **O que mede:** proporção dos passageiros do recorte classificados como sobreviventes entre os registros com classificação conhecida.
- **Por que foi escolhida:** sobrevivência é um dos resultados centrais do conjunto Titanic e ajuda a resumir a composição do recorte.
- **Público-alvo:** estudantes, docentes e pessoas interessadas em explorar o conjunto de dados.
- **Qual decisão ou interpretação pode apoiar:** permite comparar descritivamente recortes diferentes e formular perguntas para investigação posterior.
- **O que comunica:** percentual de registros classificados como sobreviventes no recorte atual.
- **Cálculo sugerido:** número de registros classificados como sobreviventes dividido pelo número de registros com `sobreviveu` conhecido, multiplicado por 100. Confirme os rótulos reais com `df["sobreviveu"].value_counts(dropna=False)` antes de implementar.
- **Limitação:** diferença de taxas entre grupos não demonstra que uma variável causou a sobrevivência.

## 3. Tarifa média

- **Variável(is) utilizada(s):** `Fare`.
- **O que mede:** média dos valores de tarifa nos registros do recorte atual.
- **Por que foi escolhida:** resume o nível médio das tarifas no grupo analisado e pode motivar comparações descritivas entre grupos.
- **Público-alvo:** estudantes, docentes e pessoas que analisam os dados históricos.
- **Qual decisão ou interpretação pode apoiar:** orienta a investigação de possíveis diferenças de tarifa entre recortes, sempre considerando outras variáveis e limitações do conjunto.
- **O que comunica:** valor médio de `Fare` para os passageiros incluídos.
- **Cálculo sugerido:** `df_filtrado["Fare"].mean()`.
- **Limitação:** mostrar a unidade conforme a documentação do dataset; não presumir moeda se ela não estiver documentada na fonte utilizada.

## 4. Idade média entre registros com idade conhecida

- **Variável(is) utilizada(s):** `Age`.
- **O que mede:** média de idade dos passageiros cujo valor de idade está preenchido.
- **Por que foi escolhida:** ajuda a descrever o perfil etário da amostra e a contextualizar as distribuições por idade.
- **Público-alvo:** estudantes, docentes e pessoas que exploram o dataset.
- **Qual decisão ou interpretação pode apoiar:** ajuda a comparar descritivamente recortes etários e a identificar perguntas para a análise exploratória.
- **O que comunica:** idade média dos passageiros com idade conhecida.
- **Cálculo sugerido:** `df_filtrado["Age"].mean()`; o Pandas ignora `NaN` ao calcular a média.
- **Limitação:** informar junto da métrica quantos passageiros tinham idade conhecida, pois o dataset tem valores ausentes em `Age`.

## Decisões de apresentação

- Mostrar entre três e cinco KPIs, conforme orientado na aula.
- Fazer os indicadores responderem aos filtros ativos, para que numerador e denominador usem o mesmo recorte.
- Indicar unidade e população considerada em cada métrica.
- Não interpretar correlação ou diferença entre grupos como prova de causalidade.
