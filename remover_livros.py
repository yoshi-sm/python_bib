from saveload import *


# remove todos os livros que vieram antes do ano limite do BD
def rmv_ano(ano_limite):
    with open("bd/categoria.dat") as f:
        cat = json.loads(f.read())
    with open("bd/tematica.dat") as f:
        tem = json.loads(f.read())
    dicionario = carregar()
    temp = []
    for i in range(len(dicionario["ano"])):
        if dicionario["ano"][i] < ano_limite:
            titulo_temp = dicionario["titulo"][i]
            temp.append(i)
            for k in cat:
                if titulo_temp in cat[k]:
                    cat[k].remove(titulo_temp)
            for k in tem:
                if titulo_temp in tem[k]:
                    tem[k].remove(titulo_temp)
    for i in reversed(temp):
        for key in dicionario:
            dicionario[key].pop(i)
    salvar(dicionario)
    with open("bd/categoria.dat", "w") as f:
        f.write(json.dumps(cat))
    with open("bd/tematica.dat", "w") as f:
        f.write(json.dumps(tem))


def rmv_titulo(titulo):
    dicionario = carregar()
    if titulo in dicionario["titulo"]:
        while titulo in dicionario["titulo"]:
            temp = dicionario["titulo"].index(titulo)
            for key in dicionario:
                dicionario[key].pop(temp)
        salvar(dicionario)
        with open("bd/categoria.dat") as f:
            cat = json.loads(f.read())
        with open("bd/tematica.dat") as f:
            tem = json.loads(f.read())
        for k in cat:
            if titulo in cat[k]:
                cat[k].remove(titulo)
        for k in tem:
            if titulo in tem[k]:
                tem[k].remove(titulo)
        with open("bd/categoria.dat", "w") as f:
            f.write(json.dumps(cat))
        with open("bd/tematica.dat", "w") as f:
            f.write(json.dumps(tem))

    else:
        print(f"O livro {titulo} não está no acervo da biblioteca.")
