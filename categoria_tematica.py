import json


bd_cat = "categoria_tematica.dat"


def reset_cat():
    vazio = []
    with open(bd_cat, "w") as f:
        f.write(f"{json.dumps(vazio)}\n{json.dumps(vazio)}")


def add_categoria(categoria):

    with open(bd_cat, "r") as f:
        categ = json.loads(f.readline())
        temat = f.readline()

    categ.append(categoria)
    with open(bd_cat, "w") as f:
        f.write(f"{json.dumps(categ)}\n{temat}")


def obter_categorias():
    with open(bd_cat, "r") as f:
        categ = json.loads(f.readline())

    return categ


def add_tematica(tematica):

    with open(bd_cat, "r") as f:
        categ = f.readline()
        temat = json.loads(f.readline())

    temat.append(tematica)
    with open(bd_cat, "w") as f:
        f.write(f"{categ}{json.dumps(temat)}")


def obter_tematicas():
    with open(bd_cat, "r") as f:
        f.readline()
        temat = json.loads(f.readline())

    return temat


