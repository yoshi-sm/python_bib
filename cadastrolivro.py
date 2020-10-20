from saveload import *



def cadastroLivros():

    #Carregando os valores no dicionario
    cadastro = carregar()

    #Adicionando novos valores no dicionario
    cadastro["titulo"].append(input('Titulo: '))
    cadastro["autores"].append(input('Autor: '))
    cadastro["categorias"].append(input('Categoria: '))
    cadastro["tematicas"].append(input('Tematica: '))
    cadastro["assuntos"].append(input('Assunto: '))
    cadastro["ano"].append(input('Ano: '))
    cadastro["localização"].append(input('Localização: '))
    cadastro["unidades"].append(input('Unidades: '))
    cadastro["data_devolução"].append(input('Data de devolução: '))
    cadastro["alugado"].append(False)
    cadastro["reservado"].append(False)

    print(cadastro)
    #Salvando os novos valores
    salvar(cadastro)


print(cadastroLivros())


