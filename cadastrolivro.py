from saveload import salvar, carregar



def cadastroLivros():

    #Carregando os valores no dicionario
    bd = carregar()

    tamanho_array = len(bd)
    #Adicionando novos valores no dicionario
    titulo = input('Titulo: ')

    # Checar se o livro já existe na base de dados:
    for i in range(tamanho_array):
        # Percorrer toda a base de dados para encontrar um livro similar
        if bd[i]["titulo"] == titulo:
            print("Livro já cadastrado!")
            # Se sim, retornar o usuário ao menu anterior
            escolha = "z"
            return escolha

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


    #print(cadastro)
    #Salvando os novos valores



#print(cadastroLivros())


