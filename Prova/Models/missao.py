from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Models.base import Base, Session

class Missao(Base):
    __tablename__ = "missoes"

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    descricao = Column(String)
    recompensa_xp = Column(Integer)
    status = Column(String)
    heroi_id = Column(Integer, ForeignKey("herois.id"))

    heroi = relationship("Heroi", back_populates="missoes")

    def concluir(self):
        self.status = "concluida"

    def resumo(self):
        return f"{self.titulo} - {self.status} (XP: {self.recompensa_xp})"