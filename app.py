import pandas as pd
import plotly.express as px
import streamlit as st

from src.data_loader import load_data

st.set_page_config(
    page_title="Análise Exploratória do Titanic",
    layout="wide",
)

st.title("Análise Exploratória do Titanic")
st.caption("Correlação e distribuição das variáveis quantitativas")

df = load_data()

VARS_QUANT = ["Age", "Fare", "SibSp", "Parch"]
COLUNA_CLASSE = "sobreviveu"

colunas_necessarias = VARS_QUANT + [COLUNA_CLASSE]
colunas_ausentes = [
    coluna for coluna in colunas_necessarias if coluna not in df.columns
]

if colunas_ausentes:
    st.error(f"Colunas ausentes no CSV: {', '.join(colunas_ausentes)}")
    st.stop()

with st.sidebar:
    st.header("Filtros")

    variaveis = st.multiselect(
        "Variáveis quantitativas",
        options=VARS_QUANT,
        default=VARS_QUANT,
    )

    separar_por_classe = st.toggle(
        "Distinguir por sobrevivência",
        value=False,
    )

    intervalos = {}

    for var in variaveis:
        serie = df[var].dropna()

        if serie.empty:
            continue

        minimo_real = float(serie.min())
        maximo_real = float(serie.max())

        if minimo_real == maximo_real:
            intervalos[var] = (minimo_real, maximo_real)
            continue

        if pd.api.types.is_integer_dtype(df[var]):
            minimo = int(minimo_real)
            maximo = int(maximo_real)
            passo = 1
        else:
            minimo = minimo_real
            maximo = maximo_real
            passo = 0.1

        intervalos[var] = st.slider(
            f"Intervalo de {var}",
            min_value=minimo,
            max_value=maximo,
            value=(minimo, maximo),
            step=passo,
            key=f"intervalo_{var}",
        )

df_filtrado = df.copy()

for var, (inicio, fim) in intervalos.items():
    serie = df[var].dropna()

    if serie.empty:
        continue

    minimo_real = float(serie.min())
    maximo_real = float(serie.max())

    if inicio > minimo_real or fim < maximo_real:
        df_filtrado = df_filtrado[df_filtrado[var].between(inicio, fim)]

st.caption(
    f"{len(df_filtrado)} de {len(df)} passageiros " "após os filtros selecionados."
)

tab_dashboard1, tab_dashboard2 = st.tabs(
    ["Dashboard 1 — Correlação e distribuição", "Dashboard 2 — KPIs"]
)

with tab_dashboard1:
    col_correlacao, col_distribuicao = st.columns([1, 1.5])

    with col_correlacao:
        st.subheader("Correlação")

        if len(variaveis) < 2:
            st.info(
                "Selecione pelo menos duas variáveis " "para calcular a correlação."
            )
        elif df_filtrado.empty:
            st.warning("Não há passageiros para os filtros escolhidos.")
        else:
            matriz = df_filtrado[variaveis].corr()

            fig_correlacao = px.imshow(
                matriz,
                text_auto=".2f",
                zmin=-1,
                zmax=1,
                color_continuous_scale=[
                    "#1D3557",
                    "#FAFAF7",
                    "#D6A23C",
                ],
                color_continuous_midpoint=0,
                labels={
                    "x": "Variável",
                    "y": "Variável",
                    "color": "Correlação",
                },
                aspect="auto",
            )

            fig_correlacao.update_layout(margin=dict(l=10, r=10, t=30, b=10))

            st.plotly_chart(
                fig_correlacao,
                use_container_width=True,
            )

    with col_distribuicao:
        st.subheader("Distribuição")

        if not variaveis:
            st.info(
                "Selecione pelo menos uma variável " "para visualizar sua distribuição."
            )
        elif df_filtrado.empty:
            st.warning("Não há passageiros para os filtros escolhidos.")
        else:
            var_hist = st.selectbox(
                "Variável para visualizar",
                options=variaveis,
            )

            dados_grafico = df_filtrado.dropna(subset=[var_hist])

            if dados_grafico.empty:
                st.warning("Não há valores disponíveis para essa variável.")
            elif var_hist in ["SibSp", "Parch"]:
                if separar_por_classe:
                    contagens = (
                        dados_grafico.groupby([var_hist, COLUNA_CLASSE])
                        .size()
                        .reset_index(name="Passageiros")
                    )

                    fig_distribuicao = px.bar(
                        contagens,
                        x=var_hist,
                        y="Passageiros",
                        color=COLUNA_CLASSE,
                        color_discrete_map={
                            "Não Sobreviveu": "#1D3557",
                            "Sobreviveu": "#D6A23C",
                        },
                        barmode="group",
                        labels={
                            var_hist: var_hist,
                            "Passageiros": "Quantidade",
                            COLUNA_CLASSE: "Sobrevivência",
                        },
                    )
                else:
                    contagens = (
                        dados_grafico[var_hist]
                        .value_counts()
                        .sort_index()
                        .rename_axis(var_hist)
                        .reset_index(name="Passageiros")
                    )

                    fig_distribuicao = px.bar(
                        contagens,
                        x=var_hist,
                        y="Passageiros",
                        labels={
                            var_hist: var_hist,
                            "Passageiros": "Quantidade",
                        },
                    )

                fig_distribuicao.update_xaxes(dtick=1)

            elif separar_por_classe:
                fig_distribuicao = px.histogram(
                    dados_grafico,
                    x=var_hist,
                    color=COLUNA_CLASSE,
                    color_discrete_map={
                        "Não Sobreviveu": "#1D3557",
                        "Sobreviveu": "#D6A23C",
                    },
                    barmode="overlay",
                    opacity=0.65,
                    nbins=30,
                    labels={
                        var_hist: var_hist,
                        "count": "Quantidade",
                        COLUNA_CLASSE: "Sobrevivência",
                    },
                )
            else:
                fig_distribuicao = px.histogram(
                    dados_grafico,
                    x=var_hist,
                    nbins=30,
                    labels={
                        var_hist: var_hist,
                        "count": "Quantidade",
                    },
                )

            fig_distribuicao.update_layout(
                xaxis_title=var_hist,
                yaxis_title="Quantidade de passageiros",
                legend_title_text="Sobrevivência",
            )

            st.plotly_chart(
                fig_distribuicao,
                use_container_width=True,
            )

with tab_dashboard2:
    st.subheader("Dashboard 2 — KPIs")
    st.info(
        "Esta seção será desenvolvida após o planejamento "
        "e a justificativa das métricas."
    )
