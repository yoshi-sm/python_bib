import json


banco_de_dados = "bd/acervo.dat"

def reset_acervo():
    with open(banco_de_dados, "w") as f:
        f.write('{"titulo": [], "autores": [], "assunto": [],'
                '"ano": [], "localizacao" : [], "data_devolucao": [],'
                '"alugado": [], "reserva": [], "usuario_reserva": []}')

#salva o dicionario parametro no arquivo "acervo.dat" no formato json
def salvar(dicionario):
    with open(banco_de_dados, "w") as f:
        f.write(json.dumps(dicionario))


#carrega o dicionario
def carregar():
    with open(banco_de_dados) as f:
        return json.loads(f.read())



