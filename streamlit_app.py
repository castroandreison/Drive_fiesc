import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Criação de um objeto de conexão.
conn = st.connection("gsheets", type=GSheetsConnection)

# Ler os dados da planilha.
df = conn.read()

# Exibir os dados no Streamlit.
st.write("Dados da Planilha:")
st.dataframe(df)

# Exibir os dados linha por linha.
st.write("Visualizando os dados linha a linha:")
for row in df.itertuples():
    st.write(f"{row[1]} tem um {row[2]}")
