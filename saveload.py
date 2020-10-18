import json


def salvar(dicionario):
    with open("testando.dat", "w") as f:
        f.write(json.dumps(dicionario))


def carregar():
    with open("testando.dat") as f:
        return json.loads(f.read())



