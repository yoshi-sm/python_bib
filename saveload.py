import json

#salva o dicionario parametro no arquivo "testando.dat" no formato json
def salvar(dicionario):
    with open("testando.dat", "w") as f:
        f.write(json.dumps(dicionario))


#carrega o dicionario
def carregar():
    with open("testando.dat") as f:
        return json.loads(f.read())



