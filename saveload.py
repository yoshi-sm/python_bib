import json


banco_de_dados = "acervo.dat"
#def reset_dicio():


#salva o dicionario parametro no arquivo "acervo.dat" no formato json
def salvar(dicionario):
    with open(banco_de_dados, "w") as f:
        f.write(json.dumps(dicionario))


#carrega o dicionario
def carregar():
    with open(banco_de_dados) as f:
        return json.loads(f.read())



