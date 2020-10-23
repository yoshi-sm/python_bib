import json
import os


bd_cat = "bd/categoria.json"
bd_tem = "bd/tematica.json"

def reset_cat():
    with open(bd_cat, "w") as f:
        f.write("[\n")


def reset_tem():
    with open(bd_tem, "w") as f:
        f.write("[\n")

# Adicionar nova categoria
def add_categoria(categoria):

    # Ler a base de dados, enumerar linhas
    with open(bd_cat, 'r') as f:
        bd = json.loads(f.read())
        tamanho_array = len(bd)
        linhas = f.readlines()

    # Se a base não estiver vazia, ela irá terminar com ]
    with open(bd_cat, 'w') as f:
        # Ler todas as linhas
        for linha in linhas:
            # Deletar o último ]
            if linha.strip('\n') != "]":
                f.write(linha)

    # Checar se a categoria já existe:
    for i in range(tamanho_array):
        if bd[i]["categoria"] == categoria:
            print("Categoria já cadastrada!")
            # Se sim, retornar o usuário ao menu anterior
            escolha = "z"
            return escolha

    dicionario = dict(
        categoria = categoria,
        livros = []
        )
    
    # Salvar na base de dados
    with open(bd_cat, 'a', encoding='utf8') as f:
        # Se a base de dados estiver vazia, adicionar chaves
        if os.stat(bd_cat).st_size == 0:
            f.write('[\n')

        else:
            # Adicionar "," e iniciar novo objeto
            f.write(",")

        f.write(json.dumps(dicionario, indent=4, ensure_ascii=False))
        # Terminar o dicionário em ]
        f.write("\n]")

    # with open(bd_cat, "r") as f:
    #     categ = json.loads(f.readline())
    
    # if categoria not in categ.keys():
    #     categ.update({categoria: []})
    #     with open(bd_cat, "w") as f:
    #         f.write(f"{json.dumps(categ)}")


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