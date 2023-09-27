from pydantic import BaseModel
from typing import Optional, List
from api.pessoa_model import Pessoa


class PessoaSchema(BaseModel):
    nome: str = 'Thiago'
    sobrenome: str = 'Lima Dyonisio'
    email: str = 'thiago.consult@gmail.com'
    celular: str = '11971862030'


class PessoaByIdSchema(BaseModel):
    id: int = 1


def serialize_pessoa(pessoa: Pessoa) -> Pessoa:
    return {
        'id': pessoa.id,
        'nome': pessoa.nome,
        'sobrenome': pessoa.sobrenome,
        'email': pessoa.email,
        'celular': pessoa.celular
    }


def serialize_pessoa_all(pessoas: List[Pessoa]) -> List[Pessoa]:
    lista = []

    for pessoa in pessoas:
        lista.append(serialize_pessoa(pessoa))

    return lista
