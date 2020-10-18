from saveload import *


def alt_quant(titulo, quantidade):
    dicionario = carregar()
    temp = dicionario["titulo"].index((titulo))
    dicionario["quantidade"][temp] = quantidade
    salvar(dicionario)

