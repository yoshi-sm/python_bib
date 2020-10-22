import json
import os

banco_de_dados = "bd/acervo.json"

# Deletar a base de dados, iniciar array
def reset_acervo():
    with open(banco_de_dados, "w") as f:
        f.write('[\n')

# Salva o dicionario parametro no arquivo "acervo.json"
def salvar(dicionario):

    # Ler a base de dados, enumerar linhas
    with open(banco_de_dados, 'r') as f:
        linhas = f.readlines()
        # # checar se o título já existe
        # if dicionario["titulo"] in f["titulo"]:
        #     print("Já cadastrado!")
        #     break

    # Se a base não estiver vazia, ela irá terminar com ]
    with open(banco_de_dados, 'w') as f:
        # Ler todas as linhas
        for linha in linhas:
            # Deletar o último ]
            if linha.strip('\n') != "]":
                f.write(linha)

    # Salvar na base de dados
    with open(banco_de_dados, 'a', encoding='utf8') as f:
        # Se a base de dados estiver vazio, adiconar chaves
        if os.stat(banco_de_dados).st_size == 0:
            f.write('[\n')

        else:
            # Adicionar , e iniciar novo objeto
            f.write(",")

        # Da Append no dicionário
        f.write(json.dumps(dicionario, indent=4, ensure_ascii=False))
        # Terminar o dicionário em ]
        f.write("\n]")


# Carrega o dicionario
def carregar():
    with open(banco_de_dados) as f:
        return json.loads(f.read())
