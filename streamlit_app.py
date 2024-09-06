
# .streamlit/secrets.toml
[connections.gsheets]
spreadsheet = "https://drive.google.com/file/d/1qG-QjfUwsXLg6eiNpOZk5teLo6Dlsb0r/view?usp=drive_link"

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Conexão com o Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Ler os dados da planilha
df = conn.read()

# Exibir os dados no Streamlit
st.write("Dados da Planilha:")
st.dataframe(df)

# Exibir os dados linha por linha
st.write("Visualizando os dados linha a linha:")
for row in df.itertuples():
    st.write(f"{row[1]} tem um {row[2]}")
