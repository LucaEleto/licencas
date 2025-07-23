import streamlit as st
import pandas as pd
import mysql.connector

con_origem = mysql.connector.connect(
host='162.241.203.62',
database='avinfo61_licencas',
user='avinfo61_servico',
password='Sclara02'
)
# Interface do Streamlit
st.image('logonova.bmp', width=100)
st.title('Licenças') 

# Entrada do usuário
consulta_sql_input = st.text_input('Pesquisar Cliente')

# Consulta SQL
consulta_sql = """
SELECT cliente, fantasia, dias 
FROM licencas_clientes 
WHERE cliente LIKE %s OR fantasia LIKE %s
"""

# Ação ao clicar no botão
if st.button('Pesquisar'):
    cursor_consulta = con_origem.cursor()
    # Passando o mesmo valor duas vezes para os dois campos do LIKE
    cursor_consulta.execute(consulta_sql, (f'%{consulta_sql_input}%', f'%{consulta_sql_input}%'))
    cliente_consulta = cursor_consulta.fetchall()
    cursor_consulta.close()

    # Exibindo os resultados
    if cliente_consulta:
        tb = pd.DataFrame(cliente_consulta, columns=['Cliente', 'Fantasia', 'Dias'])
        st.subheader('Consulta Cliente')
        st.dataframe(tb)
    else:
        st.warning("Nenhum cliente encontrado.")
