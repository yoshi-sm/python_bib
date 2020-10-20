from saveload import *


def alt_quant(titulo, quantidade):
    dicionario = carregar()
    if titulo in dicionario["titulo"]:
        temp = dicionario["titulo"].index(titulo)
        dicionario["quantidade"][temp] = quantidade
        salvar(dicionario)
    else:
        print(f"O livro {titulo} não está no acervo da biblioteca.")
