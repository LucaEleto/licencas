import streamlit as st
import pandas as pd
import licenca

def consulta_cliente():
    st.title('Licenças')
    st.consulta_sql = st.text_input('Pesquisar Cliente')
    consulta_sql = "SELECT codigo, cliente, cnpj, dias FROM licencas_clientes WHERE cliente LIKE %s"

    if st.button('Pesquisar'):
        cursor_consulta = licenca.con_origem.cursor()
        cursor_consulta.execute(consulta_sql, (f'%{st.consulta_sql}%',))
        cliente_consulta = cursor_consulta.fetchall()
        tb = pd.DataFrame(cliente_consulta, columns=['Codigo', 'Cliente', 'CNPJ', 'dias']) 
        st.markdown('''
            ## Consulta Cliente
        ''')
        st.table(tb)