import sqlite3

#1 - Conectando no BD
conexao = sqlite3.connect('titulo.db')

#2 - Criando o curso
cursor = conexao.cursor()

#3 - Iserindo Dados
cursor.execute(
    """
        INSERT INTO filmes(nome,ano, nota)
        VALUES('Superman',1990,5.0)

    """
)

#4- fechar conexao
conexao.commit()
conexao.close()
print("Dados inseridos na tabela")