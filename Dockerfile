FROM python:3.10

WORKDIR /api_pessoa

COPY . /api_pessoa

RUN pip install --no-cache-dir -r requirements.txt
