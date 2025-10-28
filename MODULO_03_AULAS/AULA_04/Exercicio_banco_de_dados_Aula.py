#imppotando a biblioteca sqlite3 SQlite com Python

import sqlite3

# instalar pip install mysql-connector-python / pip3 install mysql-connector-python
#import mysql.connector

conectar_Sqlite = sqlite3.connect("MODULO_03_AULAS/Banco_de_dados_Teste.db")
#conectar_Sqlite = sqlite3.connect("MODULO_03_AULAS/BANCO_DE_DADOS/escola_v2.db")

cursor = conectar_Sqlite.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS usuarios (
#         id INTEGER PRIMARY KEY,
#         nome TEXT,
#         idade INTEGER
#     )
# """)

#cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("João", 30))

cursor.execute("Select * from usuarios")
rows = cursor.fetchall()
for row in rows:
    print(row)

#conectar_Sqlite.closed()    

