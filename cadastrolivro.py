from saveload import *


def cadastroLivros():
    #Carregando os valores no dicionario
    cadastro = carregar()

    #Adicionando novos valores no dicionario
    titulo = input('Titulo: ')
    if titulo not in cadastro["titulo"]:
        cadastro["titulo"].append(titulo)
        cadastro["autores"].append(input('Autor: '))
        cadastro["assunto"].append(input('Assunto: '))
        cadastro["ano"].append(input('Ano: '))
        cadastro["localizacao"].append(input('Localização: '))
        cadastro["data_devolucao"].append("")
        cadastro["alugado"].append(False)
        cadastro["usuario_reserva"].append("")
        cadastro["usuario_aluguel"].append("")
        cadastro["reserva"].append(False)

        salvar(cadastro)
        print("Cadastro realizado!")
    else:
        print("Titulo já cadastrado!")


