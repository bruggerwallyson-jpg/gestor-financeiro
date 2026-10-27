#python -m streamlit run app.py
import streamlit as st

from financeiro import calcular_saldo
from banco import (
    inicializar_banco,
    adicionar_transacao,
    listar_transacoes,
    excluir_transacao,
    atualizar_transacao,
)

inicializar_banco()

st.title("Meu Gestor Financeiro")
st.write("Bem-vindo ao meu primeiro projeto de portfólio")

# 1. Cadastro de transações
st.header("Nova transação")

with st.form("form_transacao"):
    descricao = st.text_input("Descrição")

    valor = st.number_input(
        "Valor (R$)",
        min_value=1.00,
        step=10.00,
    )

    tipo = st.selectbox(
        "Tipo",
        ["receita", "despesa"],
    )

    categoria = st.text_input("Categoria")

    enviado = st.form_submit_button("Cadastrar")

if enviado:
    if not descricao.strip() or not categoria.strip():
        st.error("Preencha a descrição e a categoria.")
    else:
        adicionar_transacao(
            descricao.strip(),
            valor,
            tipo,
            categoria.strip(),
        )
        st.success("Transação cadastrada!")

# 2. Buscar transações para as ações
transacoes = listar_transacoes()

if transacoes:
    opcoes = {
        f"#{t['id']} - {t['descricao']} | R$ {t['valor']:.2f}": t["id"]
        for t in transacoes
    }

    st.header("Excluir transação")

    selecionada_exclusao = st.selectbox(
        "Escolha a transação que deseja excluir",
        options=list(opcoes.keys()),
        key="selecao_exclusao",
    )

    if st.button("Excluir transação"):
        excluir_transacao(opcoes[selecionada_exclusao])
        st.success("Transação excluída!")

    st.header("Editar transação")

    selecionada_edicao = st.selectbox(
        "Escolha a transação que deseja editar",
        options=list(opcoes.keys()),
        key="selecao_edicao",
    )

    id_edicao = opcoes[selecionada_edicao]

    transacao_edicao = next(
        t for t in transacoes if t["id"] == id_edicao
    )

    with st.form("form_editar"):
        nova_descricao = st.text_input(
            "Descrição",
            value=transacao_edicao["descricao"],
        )

        novo_valor = st.number_input(
            "Valor (R$)",
            min_value=0.01,
            value=float(transacao_edicao["valor"]),
            step=10.00,
        )

        novo_tipo = st.selectbox(
            "Tipo",
            ["receita", "despesa"],
            index=["receita", "despesa"].index(
                transacao_edicao["tipo"]
            ),
        )

        nova_categoria = st.text_input(
            "Categoria",
            value=transacao_edicao["categoria"],
        )

        salvar_edicao = st.form_submit_button("Salvar alterações")

    if salvar_edicao:
        if not nova_descricao.strip() or not nova_categoria.strip():
            st.error("Preencha a descrição e a categoria.")
        else:
            atualizar_transacao(
                id_edicao,
                nova_descricao.strip(),
                novo_valor,
                novo_tipo,
                nova_categoria.strip(),
            )
            st.success("Transação atualizada!")

# 3. Atualizar os dados exibidos
transacoes = listar_transacoes()
saldo = calcular_saldo(transacoes)

total_receitas = sum(
    t["valor"] for t in transacoes
    if t["tipo"] == "receita"
)

total_despesas = sum(
    t["valor"] for t in transacoes
    if t["tipo"] == "despesa"
)


# Agrupar despesas por categoria
despesas_por_categoria = {}

for t in transacoes:
    if t["tipo"] == "despesa":
        categoria = t["categoria"]
        valor = t["valor"]

        if categoria in despesas_por_categoria:
            despesas_por_categoria[categoria] += valor
        else:
            despesas_por_categoria[categoria] = valor


st.header("Resumo financeiro")
st.metric("Saldo atual", f"R$ {saldo:.2f}")

st.subheader("Receitas x Despesas")

dados_grafico = {
    "Tipo": ["Receitas", "Despesas"],
    "Valor": [total_receitas, total_despesas],
}

st.bar_chart(
    dados_grafico,
    x="Tipo",
    y="Valor",
)


st.subheader("Despesas por categoria")

if despesas_por_categoria:
    st.bar_chart(despesas_por_categoria)
else:
    st.info("Cadastre despesas para visualizar este gráfico.")



st.header("Histórico de transações")

if transacoes:
    # Filtro por tipo
    filtro_tipo = st.selectbox(
        "Filtrar por tipo:",
        ["Todas", "Receitas", "Despesas"]
    )

    # Criar uma lista de categorias sem repetições
    categorias = sorted(set(
        t["categoria"] for t in transacoes
    ))

    # Filtro por categoria
    filtro_categoria = st.selectbox(
        "Filtrar por categoria:",
        ["Todas"] + categorias
    )

    # Aplicar os filtros
    transacoes_filtradas = []

    for t in transacoes:
        corresponde_tipo = (
            filtro_tipo == "Todas"
            or (
                filtro_tipo == "Receitas"
                and t["tipo"] == "receita"
            )
            or (
                filtro_tipo == "Despesas"
                and t["tipo"] == "despesa"
            )
        )

        corresponde_categoria = (
            filtro_categoria == "Todas"
            or t["categoria"] == filtro_categoria
        )

        if corresponde_tipo and corresponde_categoria:
            transacoes_filtradas.append(t)

    st.dataframe(
        transacoes_filtradas,
        hide_index=True
    )

else:
    st.info("Nenhuma transação cadastrada ainda.")






