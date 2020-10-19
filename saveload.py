import json

#salva o dicionario parametro no arquivo "testando.dat" no formato json
def salvar_dicio(dicionario):
    with open("testando.dat", "w") as f:
        f.write(json.dumps(dicionario))


#carrega o dicionario
def carregar_dicio():
    with open("testando.dat") as f:
        return json.loads(f.read())



