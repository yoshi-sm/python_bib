from saveload import salvar, carregar

base_de_dados = 'bd/acervo.json'

def cadastroLivros():
    #Carregando os valores no dicionario
    bd = carregar(base_de_dados)

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

    salvar(base_de_dados, cadastro)
    print("Cadastro realizado!")
