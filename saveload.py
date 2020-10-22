import json


# banco_de_dados = "bd/acervo.dat"
banco_de_dados = "bd/acervo.json"

def reset_acervo():
    with open(banco_de_dados, "w") as f:
        f.write('Adicione um livro!')

        # '{"titulo": \n, "autores": \n, "assunto": \n,'
        # '"ano": \n, "localizacao" : \n, "data_devolucao": \n,'
        # '"alugado": \n, "reserva": \n, "usuario_reserva": \n}'

#salva o dicionario parametro no arquivo "acervo.dat" no formato json
def salvar(dicionario):
    with open(banco_de_dados, "w", encoding='utf8') as f:
        f.write(json.dumps(dicionario, ensure_ascii=False))


#carrega o dicionario
def carregar():
    with open(banco_de_dados) as f:
        return json.loads(f.read())



