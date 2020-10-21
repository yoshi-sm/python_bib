from saveload import *


def habilitar_reserva(titulo, quantidade):
    dicionario = carregar()
    if titulo in dicionario["titulo"]:
        contagem = dicionario["titulo"].count(titulo)
        indice = dicionario["titulo"].index(titulo)
        if quantidade < contagem:
            for i in range(quantidade):
                dicionario["reserva"][indice + contagem - 1 - i] = True
            salvar(dicionario)
        else:
            print("A quantidade de livros que deseja permitir reserva excede o permitido!")

    else:
        print(f"O livro {titulo} não está no acervo da biblioteca.")


def reservar(titulo, usuario):
    dicionario = carregar()
    if titulo in dicionario["titulo"]:
        indice = dicionario["titulo"].index(titulo)
        contagem = dicionario["titulo"].count(titulo)
        contagem_disponiveis = 0
        for i in range(indice, indice + contagem - 1):
            if dicionario["reserva"][i] and dicionario["usuario_reserva"][i] == "":
                contagem_disponiveis += 1
        if contagem_disponiveis == 0:
            print("Não existem cópias do livro desejado disponíveis para reserva/aluguel")
        else:
            for i in range(indice, indice + contagem - 1):
                if dicionario["reserva"][i] and dicionario["usuario_reserva"][i] == "":
                    dicionario["usuario_reserva"][i] = usuario
                    break
            salvar(dicionario)
    else:
        print(f"O livro {titulo} não está no acervo da biblioteca.")


#def cancelar_reserva(titulo, usuario):



def verificar_reserva(titulo, usuario):
    dicionario = carregar()
    if titulo in dicionario["titulo"]:
        indice = dicionario["titulo"].index(titulo)
        contagem = dicionario["titulo"].count(titulo)
        reserva_existente = 0
        for i in range(indice, indice + contagem - 1):
            if dicionario["reserva"][i] and dicionario["usuario_reserva"][i] == usuario:
                reserva_existente += 1
        if reserva_existente > 0:
            return True
        else:
            return False
    else:
        return False


def alugar(titulo, data_de_devolucao, usuario):
    dicionario = carregar()
    if titulo in dicionario["titulo"]:
        if verificar_reserva(titulo, usuario):
            indice = dicionario["titulo"].index(titulo)
            contagem = dicionario["titulo"].count(titulo)
            for i in range(indice, indice + contagem - 1):
                if dicionario["reserva"][i] and dicionario["usuario_reserva"][i] == usuario:
                    dicionario["data_devolucao"][i] = data_de_devolucao
                    break
            salvar(dicionario)

        else:
            reservar(titulo, usuario)
            indice = dicionario["titulo"].index(titulo)
            contagem = dicionario["titulo"].count(titulo)
            for i in range(indice, indice + contagem - 1):
                if dicionario["reserva"][i] and dicionario["usuario_reserva"][i] == usuario:
                    dicionario["data_devolucao"][i] = data_de_devolucao
                    break
            salvar(dicionario)

    else:
        print(f"O livro {titulo} não está no acervo da biblioteca.")