import json


def reset_cat():
    vazio = []
    with open("categoria_tematica.dat", "w") as f:
        f.write(f"{json.dumps(vazio)}\n{json.dumps(vazio)}")


def add_categoria(categoria):

    with open("categoria_tematica.dat", "r") as f:
        categ = json.loads(f.readline())
        temat = f.readline()

    categ.append(categoria)
    with open("categoria_tematica.dat", "w") as f:
        f.write(f"{json.dumps(categ)}\n{temat}")


def add_tematica(tematica):

    with open("categoria_tematica.dat", "r") as f:
        categ = f.readline()
        temat = json.loads(f.readline())

    temat.append(tematica)
    with open("categoria_tematica.dat", "w") as f:
        f.write(f"{categ}{json.dumps(temat)}")
