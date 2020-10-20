from saveload import *



def cadastroLivros():

    #Carregando os valores no dicionario
    cadastro = carregar()

    #Adicionando novos valores no dicionario
    cadastro["Titulos"].append(input('Titulo: '))
    cadastro["Autores"].append(input('Autor: '))
    cadastro["Categorias"].append(input('Categoria: '))
    cadastro["Tematicas"].append(input('Tematica: '))
    cadastro["Assuntos"].append(input('Assunto: '))
    cadastro["Ano"].append(input('Ano: '))
    cadastro["Localização"].append(input('Localização: '))
    cadastro["Unidades"].append(input('Unidades: '))
    cadastro["Data de devolução"].append(input('Data de devolução: '))
    cadastro["Alugado"].append(False)
    cadastro["Reservado"].append(False)

    print(cadastro)
    #Salvando os novos valores
    salvar(cadastro)


print(cadastroLivros())


