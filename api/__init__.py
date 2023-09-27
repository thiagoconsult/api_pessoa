from flask_openapi3 import OpenAPI, Info
from api.routes import api
from api import db, pessoa_model
from flask_cors import CORS

info = Info(title='Microserviço de Pessoa', version='1.0.1',
            description='Gestão do Cadastro de Pessoa')

app = OpenAPI(__name__, info=info)

CORS(app)

app.register_api(api)
