from saveload import *


#habilita a reserva de um titulo
def habilitar_reserva(titulo, quantidade):
    dicionario = carregar()
    if titulo in dicionario["titulo"]:
        contagem = dicionario["titulo"].count(titulo)
        indice = dicionario["titulo"].index(titulo)
        if quantidade <= contagem:
            for i in range(quantidade):
                dicionario["reserva"][indice + i] = True
            salvar(dicionario)
        else:
            print("A quantidade de livros que deseja permitir reserva excede o permitido!")

    else:
        print(f"O livro {titulo} não está no acervo da biblioteca.")


#reserva um titulo
def reservar(titulo, usuario):
    dicionario = carregar()
    if titulo in dicionario["titulo"]:
        indice = dicionario["titulo"].index(titulo)
        contagem = dicionario["titulo"].count(titulo)
        contagem_disponiveis = 0
        for i in range(indice + 1, indice + contagem):
            if dicionario["reserva"][i] and dicionario["usuario_reserva"][i] == "":
                contagem_disponiveis += 1
        if contagem_disponiveis == 0:
            print("Não existem cópias do livro desejado disponíveis para reserva")
        else:
            for i in range(indice + 1, indice + contagem):
                if dicionario["reserva"][i] and dicionario["usuario_reserva"][i] == "":
                    dicionario["usuario_reserva"][i] = usuario
                    break
            salvar(dicionario)
    else:
        print(f"O livro {titulo} não está no acervo da biblioteca.")

"""def cancelar_reserva(titulo, usuario):
    dicionario = carregar()
    if titulo in dicionario["titulo"]:
        if usuario in dicionario["usuario_reserva"]:

        else:
            print("Não existe usua")
    else:
    print(f"O livro {titulo} não está no acervo da biblioteca.")"""


#funcao a ser implementada na prox versao
def verificar_reserva(titulo, usuario):
    dicionario = carregar()
    if titulo in dicionario["titulo"]:
        indice = dicionario["titulo"].index(titulo)
        contagem = dicionario["titulo"].count(titulo)
        reserva_existente = 0
        for i in range(indice + 1, indice + contagem):
            if dicionario["reserva"][i] and dicionario["usuario_reserva"][i] == usuario:
                reserva_existente += 1
        if reserva_existente > 0:
            return True
        else:
            return False
    else:
        return False


#aluga um livro para "usuario" com "data_de_devolucao"
def alugar(titulo, data_de_devolucao, usuario):
    dicionario = carregar()
    boole = False
    if titulo in dicionario["titulo"]:
        indice = dicionario["titulo"].index(titulo)
        contagem = dicionario["titulo"].count(titulo)
        for i in range(indice + 1, indice + contagem):
            if (not dicionario["reserva"][i]) and dicionario["usuario_reserva"][i] == '':
                dicionario["alugado"][i] = True
                dicionario["data_devolucao"][i] = data_de_devolucao
                dicionario["usuario_aluguel"][i] = usuario
                salvar(dicionario)
                boole = True
                print("Aluguel realizado com sucesso!")
                break
        if not boole:
            print("Não existem exemplares deste livro disponíveis para aluguel!")

    else:
        print(f"O livro {titulo} não está no acervo da biblioteca.")
