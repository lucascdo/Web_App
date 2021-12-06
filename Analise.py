import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.sidebar.image('inovarq.jpeg')
st.image('inovarq.jpeg')
dados = pd.read_csv('dados_gorjeta.csv')

uploaded_file = st.file_uploader("Click Aqui para inserir seu arquivo")

paginas = ['Home', 'Analise Descritiva', 'Grafico']
pagina = st.sidebar.selectbox('Selecione a pagina que você deseja', paginas)

if pagina == 'Home':
	st.markdown('# Analise de Restaurante')
	
	st.write(dados)

if pagina == 'Analise Descritiva':
	var = st.sidebar.selectbox('Selecione uma variável', ['valor_da_conta', 'gorjeta', 'total_de_pessoas'])

	media = dados.groupby(['dia_da_semana', 'valor_da_conta']).mean()
	st.write(media)
	st.table(dados.describe())

if pagina == 'Grafico':
	variaveis = dados.columns.tolist()
	var1 = var = st.sidebar.selectbox('Selecione uma variável', variaveis)


	plot = dados['valor_da_conta'].plot(kind = 'barh')
	fig = plt.figure(figsize=(10, 4))
	sns.countplot(x = var1, data = dados)
	st.pyplot(fig)