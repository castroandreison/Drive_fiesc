import streamlit as st
import pygsheets
import pandas as pd

# Autenticar com o pygsheets usando o arquivo de credenciais correto
# Defina o caminho para o arquivo de credenciais
gc = pygsheets.authorize(service_file='config/credentials.json')

# Abrir a planilha pelo Google Sheets URL (pegue o ID do documento a partir do URL)
sheet_url = "https://docs.google.com/spreadsheets/d/1t2Ly9Qga99EpjUryL9pAMJU2DZxent426gVy-y0gNis/"
spreadsheet = gc.open_by_url(sheet_url)

# Selecionar a aba desejada (use o índice ou nome da aba)
worksheet = spreadsheet[0]  # ou use o nome: spreadsheet.worksheet_by_title("Nome da aba")

# Ler os dados da planilha, selecionar colunas e número de linhas
df = worksheet.get_as_df()  # Carrega os dados completos como DataFrame
df_selected = df.iloc[:3, [0, 1]]  # Seleciona as primeiras 3 linhas e colunas 0 e 1

# Exibir os dados no Streamlit
st.write("Resultados:")
for row in df_selected.itertuples():
    st.write(f"{row[1]} tem um :{row[2]}:")

# Exibir o DataFrame completo ou selecionado
st.dataframe(df_selected)
