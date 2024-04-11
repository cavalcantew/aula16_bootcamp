from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select
import sqlite3

# Defina o caminho para o arquivo .sql
arquivo_sql = 'read_sql.sql'

#engine = create_engine("sqlite:///database.db")
conexao = sqlite3.connect('database.db')

# Abra o arquivo .sql e leia seu conteúdo
with open(arquivo_sql, 'r') as arquivo:
    comandos_sql = arquivo.read()

# Execute os comandos SQL no banco de dados
conexao.executescript(comandos_sql)

# Fetch dos resultados
heroes = conexao.fetchall()

# Imprimindo os resultados
for hero in heroes:
    print(hero)