import json


bd_cat = "categoria.dat"
bd_tem = "tematica.dat"

def reset_cat():
    with open(bd_cat, "w") as f:
        f.write("{}")


def reset_tem():
    with open(bd_tem, "w") as f:
        f.write("{}")


def add_categoria(categoria):

    with open(bd_cat, "r") as f:
        categ = json.loads(f.readline())
    if categoria not in categ.keys():
        categ.update({categoria: []})
        with open(bd_cat, "w") as f:
            f.write(f"{json.dumps(categ)}")


def obter_categorias():
    with open(bd_cat, "r") as f:
        categ = json.loads(f.readline())

    return categ


def add_tematica(tematica):
    with open(bd_tem, "r") as f:
        temat = json.loads(f.readline())
    if tematica not in temat.keys():
        temat.update({tematica: []})
        with open(bd_tem, "w") as f:
            f.write(f"{json.dumps(temat)}")


def obter_tematicas():
    with open(bd_tem, "r") as f:
        temat = json.loads(f.readline())

    return temat


