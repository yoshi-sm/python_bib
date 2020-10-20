from saveload import *
from datetime import datetime
from categoria_tematica import obter_categorias, obter_tematicas


def rel_acervo():
    dicionario = carregar()
    with open(f"rel_acervo_{datetime.now().strftime('%d-%m-%Y-%f')}.txt", "w") as f:
        f.write("Código do livro               Qtd. disponível               Qtd. alugado\n\n")
        for i in range(len(dicionario["quantidade"])):
            f.write(f"{str(i).zfill(10)}{str(dicionario['quantidade'][i]).center(55)}"
                    f"{str(dicionario['quantidade_alugado'][i]).center(3)}\n")

        f.write(f"\n\n\n\nRelatorio gerado em: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")


def rel_categoria():
    dicionario = carregar()
    categorias = obter_categorias()
    with open(f"rel_categ_{datetime.now().strftime('%d-%m-%Y-%f')}.txt", "w") as f:
        for i in categorias:
            f.write(f"Categoria: {i}\n")
            if dicionario["categoria"].count(i) != 0:
                f.write("Título do livro\n\n")
                for j in range(len(dicionario["categoria"])):
                    if i == dicionario["categoria"][j]:
                        f.write(f"{dicionario['titulo'][j]}\n")
            else:
                f.write("Nenhum título com nessa categoria.")

            f.write("\n\n\n")

        f.write(f"\n\n\n\nRelatorio gerado em: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")


def rel_tematica():
    dicionario = carregar()
    tematicas = obter_tematicas()
    with open(f"rel_categ_{datetime.now().strftime('%d-%m-%Y-%f')}.txt", "w") as f:
        for i in tematicas:
            f.write(f"Tematica: {i}\n")
            if dicionario["tematica"].count(i) != 0:
                f.write("Título do livro\n\n")
                for j in range(len(dicionario["tematica"])):
                    if i == dicionario["tematica"][j]:
                        f.write(f"{dicionario['titulo'][j]}\n")
            else:
                f.write("Nenhum título com essa temática.")

            f.write("\n\n\n")
        f.write(f"\n\n\n\nRelatorio gerado em: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")