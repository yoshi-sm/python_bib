import json

banco_de_dados = "testando.dat"

#def reset_dicio():
#salva o dicionario parametro no arquivo "testando.dat" no formato json


def salvar(dicionario):
    with open(banco_de_dados, "w") as f:
        f.write(json.dumps(dicionario))


#carrega o dicionario
def carregar():
    with open(banco_de_dados) as f:
        return json.loads(f.read())



