import sqlite3

#1 - Conectando no BD
conexao = sqlite3.connect('titulo.db')

#2 - Criando o curso
cursor = conexao.cursor()

#3 - Leitura de dados
dados = cursor.execute(
    """
        Select * from filmes

    """
)

print(dados.fetchall())

#4- fechar conexao
conexao.commit()
conexao.close()
print("Dados inseridos na tabela")