import sqlite3

#1 - Conectando no BD
conexao = sqlite3.connect('titulo.db')

#2 - Criando o curso
cursor = conexao.cursor()

#3 - Criando a tabela
cursor.execute(
    """
    Create table filmes(
        id integer not null primary key autoincrement,
        nome text not null,
        ano integer not null,
        nota real not null
        );

    """
)

#4- fechar conexao
conexao.close()
print("Tabela foi criada")