from saveload import *


# remove todos os livros que vieram antes do ano limite do BD
def rmv_ano(ano_limite):
    dicionario = carregar()
    temp = []
    for i in range(len(dicionario["ano"])):
        if dicionario["ano"][i] < ano_limite:
            temp.append(i)

    for i in reversed(temp):
        for key in dicionario:
            dicionario[key].pop(i)
    salvar(dicionario)



def rmv_titulo(titulo):
    dicionario = carregar()
    temp = dicionario["titulo"].index((titulo))
    for key in dicionario:
        dicionario[key].pop(temp)
    salvar(dicionario)
