import sqlite3

def conectar():
    return sqlite3.connect("produtos.db")

def Criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produtos(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Quantidade INTEGER NOT NULL,
        Preco DECIMAL NOT NULL
        );
    """)

def Adicionar_produtos(nome, quantidade, preco):
    conn = conectar()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO Produtos (Nome, Quantidade, Preco)
            VALUES (?, ?, ?)
        """, (nome, quantidade, preco))
    except:
        conn.close()
        return False
    
    conn.commit()
    conn.close()
    return True

def Update_dados(nome, id_produto):
    conn = conectar()
    cursor = conn.cursor()  

    try:
        cursor.execute("""
            UPDATE Produtos
            SET Nome = ? WHERE id = ?
        """, (nome, id_produto))
    except:
        conn.close()
        return False
    
    conn.commit()
    conn.close()
    return True

def Update_dados2(quantidade, id_produto):
    conn = conectar()
    cursor = conn.cursor()  

    try:
        cursor.execute("""
            UPDATE Produtos
            SET Quantidade = ? WHERE id = ?
        """, (quantidade, id_produto))
    except:
        conn.close()
        return False
    
    conn.commit()
    conn.close()
    return True

def Update_dados3(preco, id_produto):
    conn = conectar()
    cursor = conn.cursor()  

    try:
        cursor.execute("""
            UPDATE Produtos
            SET Preco = ? WHERE id = ?
        """, (preco, id_produto))
    except:
        conn.close()
        return False
    
    conn.commit()
    conn.close()
    return True

def Listar_produtos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM Produtos;
    """)
    result = cursor.fetchall()
    conn.close()
    return result

def Deletar_dados(id_produto):
    conn = conectar()
    cursor = conn.cursor() 

    try:
        cursor.execute(f"""
            DELETE FROM Produtos WHERE id == {id_produto}
        """)    
    except:
        conn.close()
        return False
    
    conn.commit()
    conn.close()
    return True

def Input_dados():
    Criar_tabela()

    op = int(input("""
╔══════════════════════════════════════╗
║           MENU PRINCIPAL             ║
╠══════════════════════════════════════╣
║  1. Inserir                          ║
║  2. Listar                           ║
║  3. Atualizar                        ║
║  4. Deletar                          ║
╠══════════════════════════════════════╣
║  Escolha uma opção:                  ║
╚══════════════════════════════════════╝
"""))
    
    match op:
       
        case 1:
          
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade de produtos: "))
            preco = float(input("Digite o preço do produto: "))

            if Adicionar_produtos(nome, quantidade, preco):
                    print ("Dados do produto inseridos")
            else:
                    print("Erro ao inserir o produto")
        
        case 2:
               print(Listar_produtos()) 
        
        case 3:
            
            id_produto = int(input("Digite o id do produto para atualizar os dados: "))
            op = int(input("1. Nome\n2.Quantidade\n3.Preço\nEscolha: "))
        
            match op:
             
                case 1:
                    nome = input("Nome: ")
                    if Update_dados(nome, id_produto ):
                        print("Nome do produto atualizado")
                    else:
                        print("Não foi possivel atualizar o nome do produto")

                case 2:
                    quantidade = input("Quantidade: ")
                    if Update_dados2(quantidade, id_produto):
                        print("Quantidade de produtos atualizada")
                    else:
                        print("Não foi possivel atualizar a quantidade de produtos")

                case 3:
                    preco = input("Preço: ")
                    if Update_dados3(preco, id_produto):
                        print("Preço do produto atualizado")
                    else:
                        print("Não foi possivel atualizar o preço do produto")
        
        case 4:
            id_produto = int(input("Qual produto quer deletar\nID:"))
            if Deletar_dados(id_produto):
                print("Produto deletado")
            else:
                print("Não foi possivel deletar o produto")

if __name__ == "__main__":
    Input_dados()