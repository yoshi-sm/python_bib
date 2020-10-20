import json


bd_cat = "bd/categoria.dat"
bd_tem = "bd/tematica.dat"

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


def add_livro_categoria(titulo, categoria):

    with open(bd_cat, "r") as f:
        categ_bd = json.loads(f.readline())
    if categoria in categ_bd.keys():
        if titulo not in categ_bd[categoria]:
            categ_bd[categoria].append(titulo)
            with open(bd_cat, "w") as f:
                f.write(json.dumps(categ_bd))
        else:
            print(f'{titulo} já está em {categoria}!')

    else:
        print(f'A categoria: "{categoria}" não está cadastrada.')


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


def add_livro_tematica(titulo, tematica):
    with open(bd_tem, "r") as f:
        temat_bd = json.loads(f.readline())
    if tematica in temat_bd.keys():
        if titulo not in temat_bd[tematica]:
            temat_bd[tematica].append(titulo)
            with open(bd_tem, "w") as f:
                f.write(json.dumps(temat_bd))
        else:
            print(f'{titulo} já está em {tematica}!')

    else:
        print(f'A tematica: "{tematica}" não está cadastrada.')