import funcionarios
import cadastrolivro
import importacao
import categoria_tematica
import alterar_quantidade

def retornar():
    input("\n\nPressione qualquer tecla para continuar:")


def main():
    rodar = True
    print("Seja bem vindo ao Morais Library!")
    while rodar:

        login = funcionarios.login_func(input("Digite seu login: "), input("Digite sua senha: "))

        if login:
            print("login efetuado com sucesso!\n\n")
            escolha = "z"
            while escolha == "z":

                escolha = input("O que deseja fazer? Digite(a,b,c,d,...): "
                                "\na -Cadastrar ou Importar novos livros"
                                "\nb -Cadastrar categorias"
                                "\nc -Cadastrar tematicas"
                                "\nd -Atualizar a quantidade de unidades de um livro"
                                "\ne -Atualizar títulos que podem ser reservados"
                                "\nf -Remover títulos do acervo"
                                "\ng -Busca de livros no acervo"
                                "\nh -Obter status do livro"
                                "\ni -Gerar relátorios"
                                "\nj -Sair do sistema\n")

                while escolha == "a":

                    escolha_livro = input("O que deseja fazer? Digite(a,b,c,d,...): "
                                          "\na -Digitar manualmente os dados do livro"
                                          "\nb -Importar através de um arquivo"
                                          "\nz -Retornar ao menu anterior.")

                    if escolha_livro == "a":
                        print("Bem vindo ao cadastro manual de livros!")
                        print("Digite os valores de acordo com o solicitado:")
                        cadastrolivro.cadastroLivros()
                        retornar()
                        #print("Livro cadastrado!")

                    elif escolha_livro == "b":
                        print("Bem vindo ao cadastro de livros por importação!\n\n"
                              "O arquivo deve ser um dicionário com as chaves\n"
                              "titulo, autores, assunto, ano, localização, unidades e unidades_disponiveis.\n")
                        arquivo = input("Digite o caminho até o arquivo de importação!")
                        importacao.importa_arq(arquivo)
                        retornar()

                    elif escolha_livro == "z":
                        escolha = escolha_livro

                    else:
                        print("Opção inválida!")
                        retornar()

                while escolha == "b":
                    print("Bem vindo ao cadastro de categorias!")
                    escolha_categoria = input("O que deseja fazer agora?"
                                              "\na -Cadastrar nova categoria."
                                              "\nb -Cadastrar livro em uma categoria existente."
                                              "\nc -Obter categorias existentes."
                                              "\nz -Retornar ao menu anterior\n")

                    if escolha_categoria == "a":
                        categoria_tematica.add_categoria(input("Digite o nome da categoria que deseja adicionar: "))
                        retornar()

                    elif escolha_categoria == "b":
                        categoria_tematica.add_livro_categoria(input("Digite o nome do livro: "),
                                                               input("Digite a categoria: "))
                        retornar()

                    elif escolha_categoria == "c":
                        categorias = categoria_tematica.obter_categorias()
                        print("Categorias: ")
                        for key in categorias:
                            print(f"{key}")
                        retornar()

                    elif escolha_categoria == "z":
                        escolha = escolha_categoria

                    else:
                        print("Opção inválida!")
                        retornar()

                while escolha == "c":
                    print("Bem vindo ao cadastro de tematicas!")
                    escolha_tematica = input("O que deseja fazer agora?"
                                              "\na -Cadastrar nova tematica."
                                              "\nb -Cadastrar livro em uma tematica existente."
                                              "\nc -Obter tematicas existentes."
                                              "\nz -Retornar ao menu anterior\n")

                    if escolha_tematica == "a":
                        categoria_tematica.add_tematica(input("Digite o nome da tematica que deseja adicionar: "))
                        retornar()

                    elif escolha_tematica == "b":
                        categoria_tematica.add_livro_tematica(input("Digite o nome do livro: "),
                                                              input("Digite a tematica: "))
                        retornar()

                    elif escolha_tematica == "c":
                        tematicas = categoria_tematica.obter_tematicas()
                        print("Tematicas: ")
                        for key in tematicas:
                            print(f"{key}")
                        retornar()

                    elif escolha_tematica == "z":
                        escolha = escolha_tematica

                    else:
                        print("Opção inválida!")
                        retornar()

                while escolha == "d":
                    print("Bem vindo à atualização de unidades de livro!")
                    escolha_att_livro = input("O que deseja fazer agora?"
                                              "\na -Atualizar quantidade de livro."
                                              "\nz -Retornar ao menu anterior\n")

                    if escolha_att_livro == "a":
                        alterar_quantidade.alt_quant(input("Digite o título do livro: "),
                                                     input("Digite a nova quantidade: "))

                        retornar()

                    elif escolha_att_livro == "z":
                        escolha = escolha_tematica

                    else:
                        print("Opção inválida!")
                        retornar()

                while escolha == "j":
                    rodar = False
                    escolha = "y"
                    print("Sistema encerrando operação!")

        else:
            print("Nome de usuário ou senha incorretos, tente novamente.\n")


main()
