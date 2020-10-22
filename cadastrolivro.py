from saveload import salvar, carregar



def cadastroLivros():

    #Carregando os valores no dicionario
    # cadastro = carregar()

    #Adicionando novos valores no dicionario
    titulo = input('Titulo: ')

    # if titulo not in cadastro["titulo"]:
        # cadastro["titulo"].append(titulo)
    cadastro = dict(
        titulo = titulo,
        autores = input('Autor: '),
        assunto = input('Categoria: '),
        ano = input('Ano: '), 
        localizacao = input('Localização: '),
        data_devolucao = "",
        alugado = "",
        reserva = "",
        usuario_reserva = ""
        )

    salvar(cadastro)
    print("Cadastro realizado!")
    # else:
    #     print("Titulo já cadastrado!")

    #print(cadastro)
    #Salvando os novos valores



#print(cadastroLivros())


