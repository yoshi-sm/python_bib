from saveload import *


def status(titulo):
    dicionario = carregar()
    indice = dicionario["titulo"].index(titulo)
    lista = [dicionario["localizacao"][indice], dicionario["quantidade_disponivel"][indice],
             dicionario["quantidade_alugado"][indice], [dicionario["datas_de_devolucao"][indice]]]

    return f"Localização: {lista[0]},\n" \
           f"quantidade disponível: {lista[1]},\n" \
           f"quantidade alugado: {lista[2]},\n" \
           f"datas de devolução: {lista[3]}"
