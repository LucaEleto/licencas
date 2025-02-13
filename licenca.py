import streamlit as st
import pandas as pd
import conexao


st.title('Licenças')
st.consulta_cliente = st.text_input('Pesquisar Cliente')
consulta_cliente = "SELECT codigo, cliente, cnpj, dias FROM licencas_clientes WHERE cliente LIKE %s"

if st.button('Pesquisar'):
    cursor_consulta = conexao.con_origem.cursor()
    cursor_consulta.execute(consulta_cliente, (f'%{st.consulta_cliente}%',))
    cliente_consulta = cursor_consulta.fetchall()
    tb = pd.DataFrame(cliente_consulta, columns=['Codigo', 'Cliente', 'CNPJ', 'dias']) 
    st.header('Consulta de Cliente')
    st.table(tb)
