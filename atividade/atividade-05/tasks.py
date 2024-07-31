import sqlite3

def conectar_banco():
    """Estabelece conexão com o banco de dados SQLite e retorna o objeto de conexão e cursor."""
    conexao = sqlite3.connect('livros.db')
    cursor = conexao.cursor()
    return conexao, cursor

def criar_tabela():
    """Cria a tabela livros no banco de dados."""
    conexao, cursor = conectar_banco()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

def adicionar_livro(titulo, autor, ano):
    """Adiciona um novo livro à tabela livros."""
    conexao, cursor = conectar_banco()
    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano)
        VALUES (?, ?, ?)
    ''', (titulo, autor, ano))
    conexao.commit()
    conexao.close()

def listar_livros():
    """Lista todos os livros da tabela livros."""
    conexao, cursor = conectar_banco()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    conexao.close()
    return livros

def atualizar_livro(id, titulo, autor, ano):
    """Atualiza as informações de um livro com o ID especificado."""
    conexao, cursor = conectar_banco()
    cursor.execute('''
        UPDATE livros
        SET titulo = ?, autor = ?, ano = ?
        WHERE id = ?
    ''', (titulo, autor, ano, id))
    conexao.commit()
    conexao.close()

def deletar_livro(id):
    """Deleta um livro da tabela livros pelo ID."""
    conexao, cursor = conectar_banco()
    cursor.execute('DELETE FROM livros WHERE id = ?', (id,))
    conexao.commit()
    conexao.close()

# Exemplo de uso:
if __name__ == "__main__":
    criar_tabela()


    # Adiciona alguns livros
    adicionar_livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
    adicionar_livro('1984', 'George Orwell', 1949)
    adicionar_livro('É Assim que começa','Collen Hoover', 2022)
    
    print("Livros na tabela:")
    livros = listar_livros()
    for livro in livros:
        print(livro)
    
    print("\nAtualizando o título do livro com ID 1 para 'O Hobbit'.")
    atualizar_livro(1, 'O Hobbit', 'J.R.R. Tolkien', 1937)
    
    print("\nLivros na tabela após atualização:")
    livros = listar_livros()
    for livro in livros:
        print(livro)
    
    print("\nDeletando o livro com ID 2.")
    deletar_livro(2)
    
    print("\nLivros na tabela após deleção:")
    livros = listar_livros()
    for livro in livros:
        print(livro)