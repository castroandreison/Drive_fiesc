import streamlit as st
import gspread
import pandas as pd

# Conectar ao Google Sheets sem autenticação (para planilhas públicas)
gc = gspread.Client(auth=None)
gc.session = gspread.httpsession.HTTPSession()

# Abrir a planilha pelo URL público
spreadsheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/1t2Ly9Qga99EpjUryL9pAMJU2DZxent426gVy-y0gNis/edit?usp=sharing")
worksheet = spreadsheet.get_worksheet(0)  # Seleciona a primeira aba

# Ler os dados da planilha
data = worksheet.get_all_records()
df = pd.DataFrame(data)

# Exibir os dados no Streamlit
st.write("Dados da Planilha:")
st.dataframe(df)

# Exibir os dados linha por linha
st.write("Visualizando os dados linha a linha:")
for index, row in df.iterrows():
    st.write(f"{row['Coluna1']} tem um {row['Coluna2']}")
