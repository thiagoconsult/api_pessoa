from typing import Any
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from api.db import engine


class Base(DeclarativeBase):
    pass


class Pessoa(Base):
    __tablename__ = 'pessoa'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    sobrenome: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    celular: Mapped[int] = mapped_column(Integer)

    def __init__(self, nome: str, sobrenome: str, email: str, celular: int) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.celular = celular


Base.metadata.create_all(engine)
