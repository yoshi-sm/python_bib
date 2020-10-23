from saveload import salvar, carregar, checar_duplicata

base_de_dados = 'bd/acervo.json'

def cadastroLivros():
    titulo_livro = input('Titulo: ')
    
    # Isso pode ser melhorado
    escolha = checar_duplicata(base_de_dados, "titulo", titulo_livro)
    if escolha == "z":
        return escolha

    cadastro = dict(
                titulo = titulo_livro,
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
