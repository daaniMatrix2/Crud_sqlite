import sqlite3

#1 - Conectando no BD
conexao = sqlite3.connect('titulo.db')

#2 - Criando o curso
cursor = conexao.cursor()

#3 - Atualizar dados
id = 1,2
cursor.execute(
    """
        DELETE FROM filmes 
        WHERE id in (?,?)

    """,
    id
)

# print(dados.fetchall())

#4- fechar conexao
conexao.commit()
# conexao.close()
print("Dados excluido com sucesso!")