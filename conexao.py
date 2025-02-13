import mysql.connector
from mysql.connector import Error

try:
    con_origem = mysql.connector.connect(
    host='162.241.203.62',
    database='avinfo61_licencas',
    user='avinfo61_servico',
    password='Sclara02'
)
    print('Conexão Realizada com Sucesso!!')

except Error as e:
    print(f'Erro : {e}')