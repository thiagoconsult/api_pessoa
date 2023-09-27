from flask_openapi3 import APIBlueprint, Tag
from flask import redirect
from api.pessoa_schema import (
    PessoaSchema,
    PessoaByIdSchema
)
from api.pessoa_services import (
    service_pessoa_create,
    service_pessoa_update,
    service_pessoa_delete,
    service_pessoa_get_all,
    service_pessoa_get_by_id,
    service_pessoa_get_count
)

tag_pessoa = Tag(name='Cadastro de Pessoa',
                 description='Inclusão, Alteração, Consulta e Exclusão de pessoa')

api = APIBlueprint(
    'PESSOA',
    __name__,
    abp_tags=[tag_pessoa]
)


#######################################################################
# Redirecionamento para documentação Swagger
#######################################################################


@api.route('/')
def index():
    return redirect('/openapi/swagger')


#######################################################################
# POST - Inclusão de Pessoa
#######################################################################


@api.post(
    '/pessoa',
    summary='Inclusão de Pessoa',
    description='Rota para inclusão de pessoa pelo front-end'
)
def pessoa_create(body: PessoaSchema):
    return service_pessoa_create(body)


#######################################################################
# PUT - Alteração de Pessoa
#######################################################################


@api.put(
    '/pessoa',
    summary='Alteração de Pessoa',
    description='Rota para alteração de pessoa pelo front-end'
)
def pessoa_update(query: PessoaByIdSchema, body: PessoaSchema):
    return service_pessoa_update(query, body)


#######################################################################
# DELETE - Exclusão de Pessoa
#######################################################################


@api.delete(
    '/pessoa',
    summary='Exclusão de Pessoa',
    description='Rota para exclusão de pessoa pelo front-end'
)
def pessoa_delete(query: PessoaByIdSchema):
    return service_pessoa_delete(query)


#######################################################################
# GET ALL - Consulta lista de Pessoas
#######################################################################


@api.get(
    '/pessoa/all',
    summary='Consulta lista de Pessoas',
    description='Rota para consulta de lista de pessoas pelo front-end'
)
def pessoa_get_all():
    return service_pessoa_get_all()


#######################################################################
# GET BY ID - Consulta de Pessoa por ID
#######################################################################


@api.get(
    '/pessoa/id',
    summary='Consulta de Pessoa por ID',
    description='Rota para consulta de de pessoa por ID pelo front-end'
)
def pessoa_get_by_id(query: PessoaByIdSchema):
    return service_pessoa_get_by_id(query)


#######################################################################
# GET - Consulta quantidade de Pessoas
#######################################################################


@api.get(
    '/pessoa/count',
    summary='Consulta quantidade de pessoas cadastradas',
    description='Rota para consulta de quantidade de pessoas cadastradas'
)
def pessoa_get_count():
    return service_pessoa_get_count()
