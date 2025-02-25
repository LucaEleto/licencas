import streamlit as st
import pandas as pd
import mysql.connector

con_origem = mysql.connector.connect(
host='162.241.203.62',
database='avinfo61_licencas',
user='avinfo61_servico',
password='Sclara02'
)
st.image('logonova.bmp', width=100)
st.title('Licenças') 
st.consulta_sql = st.text_input('Pesquisar Cliente')
consulta_sql = "SELECT cliente, fantasia, dias FROM licencas_clientes WHERE cliente LIKE %s"
if st.button('Pesquisar'):
    cursor_consulta = con_origem.cursor()
    cursor_consulta.execute(consulta_sql, (f'%{st.consulta_sql}%',))
    cliente_consulta = cursor_consulta.fetchall()
    tb = pd.DataFrame(cliente_consulta, columns=[ 'Cliente', 'Fantasia', 'dias'])
    st.markdown('''
        ## Consulta Cliente
    ''')
    st.data_editor(tb)
