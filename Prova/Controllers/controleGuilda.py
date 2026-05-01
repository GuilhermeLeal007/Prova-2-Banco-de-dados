from Models.base import Base, Session
from Models.heroi import Heroi
from Models.missao import Missao

class controleGuilda:

    def __init__(self):
        self.session = Session()

    def registrar_heroi(self, nome, classe):
        heroi = Heroi(nome=nome, classe=classe, nivel=1, pontos_experiencia=0)
        self.session.add(heroi)
        self.session.commit()

    def listar_herois(self):
        return self.session.query(Heroi).all()

    def buscar_heroi(self, id):
        return self.session.query(Heroi).filter_by(id=id).first()

    def remover_heroi(self, id):
        heroi = self.buscar_heroi(id)
        if heroi:
            self.session.delete(heroi)
            self.session.commit()

    def criar_missao(self, titulo, descricao, recompensa_xp, heroi_id):
        missao = Missao(
            titulo=titulo,
            descricao=descricao,
            recompensa_xp=recompensa_xp,
            status="pendente",
            heroi_id=heroi_id
        )
        self.session.add(missao)
        self.session.commit()

    def concluir_missao(self, missao_id):
        missao = self.session.query(Missao).filter_by(id=missao_id).first()

        if missao:
            if missao.status == "concluida":
                print("Missão já foi concluída!")
            else:
                missao.concluir()
                heroi = missao.heroi
                heroi.ganhar_experiencia(missao.recompensa_xp)
                self.session.commit()