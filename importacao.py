from saveload import *
import json


def importa_arq(arquivo):
    dicionario = carregar()
    with open(arquivo) as f:
        temp_arq = json.loads(f.read())

        if temp_arq.keys() == dicionario.keys():
            for key in temp_arq:
                for i in range(len(temp_arq[key])):
                    dicionario[key].append(temp_arq[key][i])

        else:
            print("arquivo incompativel com o formato do banco de dados!")

    salvar(dicionario)


