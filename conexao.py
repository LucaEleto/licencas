import mysql.connector
from mysql.connector import Error
import streamlit as st

try:
    con_origem = mysql.connector.connect(
    host='st.write("host")',
    database='st.write("database")',
    user='st.write("user")',
    password='st.write("password")'
)
    print('Conexão Realizada com Sucesso!!')

except Error as e:
    print(f'Erro : {e}')