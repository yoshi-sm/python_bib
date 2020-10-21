from saveload import *


def status(titulo):
    dicionario = carregar()
    if titulo in dicionario["titulo"]:

        indice = dicionario["titulo"].index(titulo)
        contar_titulo = dicionario["titulo"].count(titulo)
        lista_main = []
        string_print = "Lista de livros:\n\n"
        for i in range(indice, indice + contar_titulo - 1):
            lista = [dicionario["localizacao"][i], dicionario["reserva"][i],
                     dicionario["alugado"][i], dicionario["data_devolucao"][i]]
            lista_main.append(lista)

        for i in lista_main:
            if i[1]:
                i[1] = "Sim"
            else:
                i[1] = "Não"

            if i[2]:
                i[2] = "Sim"
            else:
                i[2] = "Não"

            if i[3] == '':
                i[3] = "-"

            string_print += f"Titulo: {titulo}, localização: {i[0]}, reservável: {i[1]}, alugado: {i[2]}, " \
                            f"data de devolução: {i[3]}\n"

        return string_print

    else:
        print(f"O livro {titulo} não está no acervo da biblioteca.")