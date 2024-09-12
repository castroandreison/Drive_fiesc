import streamlit as st
from st_files_connection import FilesConnection

# Tentar criar o objeto de conexão e ler o arquivo CSV
try:
    # Criar o objeto de conexão e recuperar o conteúdo do arquivo
    conn = st.connection('gcs', type=FilesConnection)
    df = conn.read("streamlit-bucket/fiesc.csv", input_format="csv", ttl=600)
    
    # Verificar se as colunas necessárias estão presentes
    if 'n' in df.columns and 'amplitude' in df.columns:
        # Se as colunas estiverem presentes, imprimir os resultados
        for row in df.itertuples():
            st.write(f"{row.n} has a :{row.amplitude}:")
    else:
        # Se as colunas não forem encontradas, exibir uma mensagem de erro
        st.error("As colunas 'n' e 'amplitude' não foram encontradas no arquivo CSV.")

# Tratar possíveis exceções de leitura de arquivos ou problemas de conexão
except Exception as e:
    st.error(f"Ocorreu um erro ao ler o arquivo CSV: {e}")
