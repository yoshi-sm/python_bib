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
        cadastro["localizacao"].append(input('Localização: '))
        #cadastro["unidades"].append(int(input('Unidades: ')))
        #unidades_reserva = int(input("Unidades para reserva/aluguel: "))
        #while unidades_reserva >= cadastro["unidades"][-1]:
        #    print("valor para unidades para reserva/aluguel inválido, tente novamente: ")
        #    unidades_reserva = int(input("Unidades para reserva/aluguel: "))
        #cadastro["unidades_reserva"].append(unidades_reserva)
        cadastro["data_devolucao"].append("")
        cadastro["alugado"].append(False)
        cadastro["usuario_reserva"].append("")
        cadastro["reserva"].append(False)

        salvar(cadastro)
        print("Cadastro realizado!")
    else:
        print("Titulo já cadastrado!")

    #print(cadastro)
    #Salvando os novos valores



#print(cadastroLivros())


