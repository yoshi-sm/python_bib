from saveload import *
import json


def importa_arq(arquivo):
    dicionario = carregar()
    with open(arquivo) as f:
        temp_arq = json.loads(f.read())
        for key in temp_arq:
            for i in range(len(temp_arq[key])):
                dicionario[key].append(temp_arq[key][i])

    salvar(dicionario)


