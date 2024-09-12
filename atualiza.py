import sqlite3

#1 - Conectando no BD
conexao = sqlite3.connect('titulo.db')

#2 - Criando o curso
cursor = conexao.cursor()

#3 - Atualizar dados
id = 1
dados = cursor.execute(
    """
        UPDATE filmes SET nome = ?
        WHERE id = ?

    """,
    ("Homem Aranha",id)
)

# print(dados.fetchall())

#4- fechar conexao
conexao.commit()
# conexao.close()
print("Dados atualizados")