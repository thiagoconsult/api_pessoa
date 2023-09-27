from api.pessoa_model import Pessoa
from api.pessoa_schema import (
    PessoaSchema,
    serialize_pessoa,
    serialize_pessoa_all
)
from api.db import engine
from sqlalchemy.orm import Session


#######################################################################
# POST - Serviço para Inclusão de Pessoa
#######################################################################


def service_pessoa_create(body: PessoaSchema):
    try:
        with Session(engine) as session:
            pessoa = Pessoa(
                nome=body.nome,
                sobrenome=body.sobrenome,
                email=body.email,
                celular=body.celular
            )

            session.add(pessoa)
            session.commit()
            return serialize_pessoa(pessoa), 201

    except Exception as e:
        return {'err': f'Falha ao cadastrar pessoa, detalhe: {e.args}'}, 400


#######################################################################
# PUT - Serviço para Alteração de Pessoa
#######################################################################


def service_pessoa_update(query, body: PessoaSchema):
    with Session(engine) as session:
        pessoa = session.query(Pessoa).filter(Pessoa.id == query.id).first()

        if not pessoa:
            return {'err': 'Pessoa não encontrada'}, 404

        try:
            pessoa.nome = body.nome
            pessoa.sobrenome = body.sobrenome
            pessoa.email = body.email
            pessoa.celular = body.celular

            session.commit()

            return serialize_pessoa(pessoa), 200

        except Exception as e:
            return {'err': f'Falha ao tentar atualizar pessoa, detalhe: {e.args}'}, 400


#######################################################################
# DELETE - Serviço para Exclusão de Pessoa
#######################################################################


def service_pessoa_delete(query):
    with Session(engine) as session:
        pessoa = session.query(Pessoa).filter(Pessoa.id == query.id).first()

        if not pessoa:
            return {'err': 'Pessoa não encontrada'}, 404

        try:
            session.delete(pessoa)
            session.commit()
            return {'Pessoa excluída com sucesso': serialize_pessoa(pessoa)}, 200

        except Exception as e:
            return {'err': f'Falha ao tentar excluir pessoa, detalhe: {e.args}'}, 400


#######################################################################
# GET ALL - Serviço para Consulta de lista de Pessoas
#######################################################################


def service_pessoa_get_all():
    with Session(engine) as session:
        pessoas = session.query(Pessoa).all()

        if not pessoas:
            return {'err': 'Nenhuma pessoa encontrada'}, 404

        return serialize_pessoa_all(pessoas), 200


#######################################################################
# GET BY ID - Serviço para Consulta de Pessoa por ID
#######################################################################


def service_pessoa_get_by_id(query):
    with Session(engine) as session:
        pessoa = session.query(Pessoa).filter(Pessoa.id == query.id).first()

        if not pessoa:
            return {'err': 'Pessoa não encontrada'}, 404

        return serialize_pessoa(pessoa), 200


#######################################################################
# GET - Serviço para Consulta Quantidade de Pessoas
#######################################################################


def service_pessoa_get_count():
    with Session(engine) as session:
        pessoas = session.query(Pessoa).all()

        # if not pessoas:
        #     return {'err': 'Nenhuma pessoa encontrada'}, 404

        quantidade = 0

        for pessoa in pessoas:
            quantidade += 1
            print(quantidade)

        return {'quantidade': quantidade}
