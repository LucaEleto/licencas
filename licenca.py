import streamlit as st
import pandas as pd
from consulta import consulta_cliente
import conexao

st.sidebar.image('logonova.bmp', width=150)
st.sidebar.markdown('''
    # Licenças Avinfo
    ''')
#Login Sistema
st.sidebar.markdown('''
    ## Login    
    ''')
usuario = st.sidebar.text_input('Usuário')
senha = st.sidebar.text_input('Senha', type='password')
if st.sidebar.button('Entrar'):
    cursor_login = conexao.con_origem.cursor()
    cursor_login.execute('SELECT * FROM acessos WHERE usuario = %s AND senha = %s', (usuario, senha))
    login = cursor_login.fetchone()
    if login:
        st.sidebar.success('Login efetuado com sucesso!')
        consulta_cliente() #Funcao de consulta
    else:
        st.sidebar.error('Usuário ou senha incorretos!')
