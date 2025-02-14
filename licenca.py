import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error


try:
    con_origem = mysql.connector.connect(
        host='162.241.203.62',
        database='avinfo61_licencas',
        user='avinfo61_servico',
        password='Sclara02'
    )

#Login Sistema

    st.sidebar.image('logonova.bmp', width=150)
    st.sidebar.markdown('''
    # Licenças Avinfo
    ''')
    st.sidebar.markdown('''
    ## Login    
    ''')
    usuario = st.sidebar.text_input('Usuário')
    senha = st.sidebar.text_input('Senha', type='password')
    if st.sidebar.button('Entrar'):
        cursor_login = con_origem.cursor()
        cursor_login.execute('SELECT * FROM acessos WHERE usuario = %s AND senha = %s', (usuario, senha))
        login = cursor_login.fetchone()
        if login:
            st.sidebar.success('Login efetuado com sucesso!') 
            #Consulta cliente
            st.title('Licenças')
            st.consulta_cliente = st.text_input('Pesquisar Cliente')
            consulta_cliente = "SELECT codigo, cliente, cnpj, dias FROM licencas_clientes WHERE cliente LIKE %s"
            if st.button('Pesquisar'):
                cursor_consulta = con_origem.cursor()
                cursor_consulta.execute(consulta_cliente, (f'%{st.consulta_cliente}%',))
                cliente_consulta = cursor_consulta.fetchall()
                tb = pd.DataFrame(cliente_consulta, columns=['Codigo', 'Cliente', 'CNPJ', 'dias']) 
                st.markdown('''
                    ## Consulta Cliente
                ''')
                st.table(tb)
        else:
            st.sidebar.error('Usuário ou senha incorretos!')

    
    

except Error as e:
    print(f'Erro : {e}')
