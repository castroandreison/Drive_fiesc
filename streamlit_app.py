
# .streamlit/secrets.toml
[connections.gsheets]
spreadsheet = "https://docs.google.com/spreadsheets/d/1t2Ly9Qga99EpjUryL9pAMJU2DZxent426gVy-y0gNis/edit?usp=sharing"

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
