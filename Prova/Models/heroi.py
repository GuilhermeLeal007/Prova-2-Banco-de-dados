from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Models.base import Base

class Heroi(Base):
    __tablename__ = "herois"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    classe = Column(String)
    nivel = Column(Integer)
    pontos_experiencia = Column(Integer)

    missoes = relationship("Missao", back_populates="heroi")

    def ganhar_experiencia(self, xp):
        self.pontos_experiencia += xp
        while self.pontos_experiencia >= 100:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.pontos_experiencia -= 100

    def resumo(self):
        return f"{self.nome} ({self.classe}) - Nível {self.nivel} | XP {self.pontos_experiencia}"
