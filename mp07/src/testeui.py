import streamlit as st
from indices import taxa_mensal_rendimento
from indices import gastos
from simulador import simular_mes_populacao
from dados import carregar_dados # chamar a função para preencher a lista pessoas antes da seleção do menu
from dados import salvar_dados_pessoas # chamar a função para salvar os dados no arquivo txt
from pessoa import Pessoa
from dados import inserir_pessoa # função para inserir nova pessoa no txt
#---------------------
#manter valor da variavel mesmo após os eventos:
if "pessoas" not in st.session_state:
    st.session_state.pessoas = [] #lista vazia para armazenar os objetos pessoa
    st.session_state.dados_carregados_tela = False #controle para exibir a tabela apenas após carregar os dados

    st.session_state.avisos_simulacao = [] #lista vazia para armazenar avisos da simulação
#dremovi o dicionário com os dados da tabela
#---------------------
#abas de navegação
abas = st.tabs(["Intro", "Dados", "Adicionar"])
#aba home ----
with abas[0]:
    st.header(f"Bem Vindo ao Simulador de Finanças")
    st.text(f"Este aplicativo permite que você simule as "
            f"finanças de várias pessoas. \n "
            f"Use as abas acima para navegar pelas funcionalidades disponíveis")
#aba secundária ----
with abas[1]:
    st.header("mostrar Dados das Pessoas", )     
#botão de carregar dados
    st.button(f"Carregar Dados", on_click=lambda:( 
              st.session_state.__setitem__("pessoas",carregar_dados( )),# dados.py resolve o caminho e a função foi importada
              st.session_state.__setitem__("dados_carregados_tela", True), #ajuste para não expor a tabela
              st.toast(f"{len(st.session_state.pessoas)}" 
                       f"pessoas carregadas com sucesso!")))#notificação
#botão de simular mês
    st.button(f"Simular Mês", on_click=lambda: (
                    st.session_state.__setitem__("avisos_simulacao", #armazena os avisos da simulação
                    simular_mes_populacao(st.session_state.pessoas, taxa_mensal_rendimento , gastos)[0]), #puxa os avisos da simulação e os parâmetros
                    st.toast("simulação concluida com sucesso!")))#notificação
   
#botão de salvar dados   
    st.button(f"Salvar Dados")
    #substitui o dicionário e st.table(dados_tabela)
    if st.session_state.dados_carregados_tela: #exibe a tabela apenas após carregar os dados
        if st.session_state.pessoas:#verifica se há pessoas na lista(são carregadasno início da página)
            nomes= [pessoa.nome for pessoa in st.session_state.pessoas]
            salarios = [f"{pessoa.salario:,.2f}" for pessoa in st.session_state.pessoas]
            patrimonio = [f"{pessoa.patrimonio:,.2f}" for pessoa in st.session_state.pessoas]
            #dicionário
            dados_tabela = {
                "Nome": nomes,
                "Salário (R$)": salarios,
                "patrimônio:(R$)" : patrimonio
            }   
            st.table(dados_tabela)
#aba de adição---       
with abas[2]:
    st.header("Adicionar nova Pessoa")

    nome = st.text_input("Nome da Pessoa")
    salario = float(st.text_input("Salário Mensal (R$)"," 0.00"))
    patrimonio = float(st.text_input("Patrimônio Inicial (R$)"," 0.00"))

    st.button("Adicionar Pessoa", on_click=lambda:(
              inserir_pessoa(nome, salario, patrimonio),
              #atualiza a lista de pessoas no streamlit
              st.session_state.__setitem__("pessoas", carregar_dados()),
              st.toast(f"Pessoa {nome} adicionada com sucesso!")))#notificação
