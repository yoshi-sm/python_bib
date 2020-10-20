from saveload import *



def cadastroLivros():

    #Carregando os valores no dicionario
    cadastro = carregar()

    #Adicionando novos valores no dicionario
    titulo = input('Titulo: ')
    if titulo not in cadastro["titulo"]:
        cadastro["titulo"].append(titulo)
        cadastro["autores"].append(input('Autor: '))
        #cadastro["categorias"].append(input('Categoria: '))
        #cadastro["tematicas"].append(input('Tematica: '))
        cadastro["assunto"].append(input('Assunto: '))
        cadastro["ano"].append(input('Ano: '))
        cadastro["localização"].append(input('Localização: '))
        cadastro["unidades"].append(input('Unidades: '))
        cadastro["unidades_disponiveis"] = cadastro["unidades"]
        #cadastro["data_devolução"].append(input('Data de devolução: '))
        #cadastro["alugado"].append(False)
        #cadastro["reservado"].append(False)

        salvar(cadastro)
        print("Cadastro realizado!")
    else:
        print("Titulo já cadastrado!")

    #print(cadastro)
    #Salvando os novos valores



#print(cadastroLivros())


