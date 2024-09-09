import streamlit as st
import pygsheets
import pandas as pd

# Autenticar com o pygsheets usando o arquivo de credenciais correto
gc = pygsheets.authorize(service_file="C:/Users/an053116/Documents/FIESC/cred.json")

# URL do Google Sheets
sheet_url  = "https://docs.google.com/spreadsheets/d/1t2Ly9Qga99EpjUryL9pAMJU2DZxent426gVy-y0gNis/"
spreadsheet = gc.open_by_url(sheet_url)

# Selecionar a primeira aba da planilha (ou escolha pelo nome da aba)
worksheet = spreadsheet[0]

# Ler os dados da planilha e selecionar colunas específicas (colunas 0 e 5)
df = worksheet.get_as_df()  # Ou usar parameters como start, end para delimitar as colunas

# Selecionar colunas 0 e 5
df_selected = df.iloc[:, [0,1,2,3,4, 5]]

# Exibir os dados no Streamlit
st.dataframe(df_selected)
