from Models.base import Base, engine
from Controllers.controleGuilda import controleGuilda
Base.metadata.create_all(engine)

guilda = controleGuilda()


def menu():
    while True:
        print("\n=== GUILDA DOS HEROIS ===")
        print("1 Registrar Heroi")
        print("2 Listar Herois")
        print("3 Criar Missão")
        print("4 Concluir Missão")
        print("0 Sair")

        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            classe = input("Classe: ")
            guilda.registrar_heroi(nome, classe)

        elif op == "2":
            herois = guilda.listar_herois()
            for h in herois:
                print(" ", h.resumo())
                for m in h.missoes:
                    print(" ", m.resumo())

        elif op == "3":
            titulo = input("Título: ")
            desc = input("Descrição: ")
            xp = int(input("XP: "))
            heroi_id = int(input("ID do herói: "))
            guilda.criar_missao(titulo, desc, xp, heroi_id)

        elif op == "4":
            id_missao = int(input("ID da missão: "))
            guilda.concluir_missao(id_missao)

        elif op == "0":
            break


menu()