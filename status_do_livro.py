from saveload import *


def status(titulo):
    dicionario = carregar()
    if titulo in dicionario["titulo"]:

        indice = dicionario["titulo"].index(titulo)
        contar_titulo = dicionario["titulo"].count(titulo)
        lista_main = []
        string_print = "Lista de livros:\n\n"
        for i in range(indice, indice + contar_titulo - 1):
            lista = [dicionario["localizacao"][i], dicionario["reservado"][i],
                     dicionario["alugado"][i], [dicionario["data_devolucao"][i]]]
            lista_main.append(lista)

        for i in lista_main:
            string_print += f"Titulo: {titulo}, localização: {i[0]}, reservado: {i[1]}, alugado: {i[2]}," \
                            f"data de devolução: {i[3]}\n"

        return string_print

    else:
        print(f"O livro {titulo} não está no acervo da biblioteca.")