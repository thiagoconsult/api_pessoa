# MICROSERVIÇO PESSOA

Esta API foi desenvolvida para entrega do MVP da Sprint 3 da PUC-RIO. Ela foi desenvolvida em Flask para servir uma aplicação
desenvolvida em React.

### Esta API trás os seguintes métodos:

| Método            | Funcionalidade                         |
| ----------------- | -------------------------------------- |
| pessoa_create     | Inclusão de uma nova pessoa            |
| pessoa_update     | Atualização de uma pessoa existente    |
| pessoa_delete     | Exclusão de uma pessoa existente       |
| pessoa_get_by_id  | Consulta uma pessoa pelo ID            |
| pessoa_get_all    | Consulta lista de pessoas cadastradas  |
| ----------------- | -------------------------------------- |

# Como executar

Você precisa ter todas as libs utilizadas no projeto e que estão listadas no arquivo requirements.txt.

Para executar este projeto você poderá criar um ambiente virtual primeiramente e ativá-lo.

### Para instalar e ativar a virtual env no Linux:

Na raiz do projeto, exexute:

```
python3 -m venv env
```

Para ativar a env, execute:

```
source env/bin/activate
```

### Instalando o projeto:

Quando a virtual env estiver ativa, irá aparecer antes do caminho do projeto no cmd o nome (env). Agora, é necessário instalar as libs:

```
pip install -r requirements.txt
```

### EXECUTANDO

Execute o comando:

```
python3 run.py
```

```
http://127.0.0.1:5002/
```

Esta página permitirá explorar a documentação do Microserviço
