import streamlit as st

nomes= []
salarios = []
patrimonios = []

#dicionário com os dados da tabela
dados_tabela = {
    "Nome": nomes, #lista de nomes
    "Salário": salarios, #lista de salários
    "Patrimônio": patrimonios #lista de patrimônios
}



abas = st.tabs(["Intro", "Dados", "Adicionar"])

with abas[0]:
    st.header(f"Bem Vindo ao Simulador de Finanças")
    st.text(f"Este aplicativo permite que você simule as "
            f"finanças de várias pessoas. \n "
            f"Use as abas acima para navegar pelas funcionalidades disponíveis")

with abas[1]:
    st.header("mostrar Dados das Pessoas")
    st.button(f"Carregar Dados")
    st.button(f"Simular Mês")
    st.button(f"Salvar Dados")

    st.table(dados_tabela)

with abas[2]:
    st.header("Adicionar nova Pessoa")

    nome = st.text_input("Nome da Pessoa")
    salario = float(st.text_input("Salário Mensal (R$)"," 0.00"))

    st.button("Adicionar Pessoa")
    