import json
import os

# banco_de_dados = "bd/acervo.dat"
banco_de_dados = "bd/acervo.json"

# TODO - Precisa de trabalho aqui
def reset_acervo():
    with open(banco_de_dados, "w") as f:
        f.write('[\n')

        # '{"titulo": \n, "autores": \n, "assunto": \n,'
        # '"ano": \n, "localizacao" : \n, "data_devolucao": \n,'
        # '"alugado": \n, "reserva": \n, "usuario_reserva": \n}'

#salva o dicionario parametro no arquivo "acervo.dat" no formato json
def salvar(dicionario):
    # Ler a base de dados
    with open(banco_de_dados, 'r') as f:
        linhas = f.readlines()

    # Se a base não estiver vazia, ela irá terminar com ]
    # Deletar o último ]
    with open(banco_de_dados, 'w') as f:
            for linha in linhas:
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


#carrega o dicionario
def carregar():
    with open(banco_de_dados) as f:
        return json.loads(f.read())



