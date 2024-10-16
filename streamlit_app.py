import streamlit as st

from streamlit_gsheets import GSheetsConnection

# Create GSheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Read Google WorkSheet as DataFrame
df = conn.read(
    worksheet="0",
    usecols=[
        0,
        1,
    ],  # specify columns which you want to get, comment this out to get all columns
)

# Display our Spreadsheet as st.dataframe
st.dataframe(df)
