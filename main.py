import funcionarios
import cadastrolivro
import importacao
import categoria_tematica
import alterar_quantidade
import remover_livros
import busca_dados
import alugar_reservar
import status_do_livro
import relatorios

#logins : senhas -> yoshi : 1234, fernando : abcd, pedro : okok
def retornar():
    input("\n\nPressione 'Enter' para continuar:")


def main():
    rodar = True
    print("Seja bem vindo ao Morais Library!")
    while rodar:
        #auteticacao de login
        login = funcionarios.login_func(input("Digite seu login: "), input("Digite sua senha: "))

        if login:
            print("login efetuado com sucesso!\n\n")
            escolha = "z"
            while escolha == "z":
                #opcoes do menu principal
                print("===============================================\n"
                      "        SEJA BEM VINDO A MORAIS LIBRARY        \n"
                      "===============================================")
                escolha = input("O que deseja fazer? Digite(a,b,c,d,...): "
                                "\na -Cadastrar ou Importar novos livros"
                                "\nb -Cadastrar categorias"
                                "\nc -Cadastrar tematicas"
                                "\nd -Atualizar a quantidade de unidades de um livro"
                                "\ne -Remover títulos do acervo"
                                "\nf -Busca de livros no acervo"
                                "\ng -Alugar,reservar ou habilitar reserva de livro"
                                "\nh -Obter status do livro"
                                "\ni -Gerar relátorios"
                                "\nj -Sair do sistema\n"
                                "ESCOLHA: ")

                while escolha == "a":
                    #opcoes do menu "a"
                    print("===============================================")
                    print("       Cadastrar ou Importar novos livros       ")
                    print("===============================================")
                    escolha_livro = input("O que deseja fazer? Digite(a,b,c,d,...): "
                                          "\na -Digitar manualmente os dados do livro"
                                          "\nb -Importar através de um arquivo"
                                          "\nz -Retornar ao menu anterior.\n"
                                          "ESCOLHA: ")

                    if escolha_livro == "a":
                        print("----------------------------------------------")
                        print("    Bem vindo ao cadastro manual de livros!    ")
                        print("----------------------------------------------")
                        print("Digite os valores de acordo com o solicitado:")
                        cadastrolivro.cadastroLivros()
                        retornar()
                        #print("Livro cadastrado!")

                    elif escolha_livro == "b":
                        print("----------------------------------------------")
                        print("Bem vindo ao cadastro de livros por importação!")
                        print("----------------------------------------------")
                        print("O arquivo deve ser um dicionário com as chaves\n"
                              "titulo, autores, assunto, ano, localização, data_de_devolução, alugado, reservado.\n")
                        arquivo = input("Digite o caminho até o arquivo de importação!")
                        importacao.importa_arq(arquivo)
                        retornar()

                    elif escolha_livro == "z":
                        escolha = escolha_livro

                    else:
                        print("Opção inválida!")
                        retornar()
                #menu b
                while escolha == "b":
                    print("===============================================")
                    print("     Bem vindo ao cadastro de categorias!     ")
                    print("===============================================")
                    escolha_categoria = input("O que deseja fazer agora?"
                                              "\na -Cadastrar nova categoria."
                                              "\nb -Cadastrar livro em uma categoria existente."
                                              "\nc -Obter categorias existentes."
                                              "\nz -Retornar ao menu anterior\n"
                                              "ESCOLHA: ")

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
                #menu c
                while escolha == "c":
                    print("===============================================")
                    print("      Bem vindo ao cadastro de tematicas!      ")
                    print("===============================================")
                    escolha_tematica = input("O que deseja fazer agora?"
                                             "\na -Cadastrar nova tematica."
                                             "\nb -Cadastrar livro em uma tematica existente."
                                             "\nc -Obter tematicas existentes."
                                             "\nz -Retornar ao menu anterior\n"
                                             "ESCOLHA: ")

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

                #menu d
                while escolha == "d":
                    print("===============================================")
                    print(" Bem vindo à atualização de unidades de livro! ")
                    print("===============================================")
                    escolha_att_livro = input("O que deseja fazer agora?"
                                              "\na -Atualizar quantidade de livro."
                                              "\nz -Retornar ao menu anterior\n"
                                              "ESCOLHA: ")

                    if escolha_att_livro == "a":
                        alterar_quantidade.alt_quant(input("Digite o título do livro: "),
                                                     int(input("Digite a quantidade a adicionar: ")))
                        retornar()

                    elif escolha_att_livro == "z":
                        escolha = escolha_att_livro

                    else:
                        print("Opção inválida!")
                        retornar()

                #menu e
                while escolha == "e":
                    print("===============================================")
                    print("    Bem vindo à remoção de livros do acervo!    ")
                    print("===============================================")
                    escolha_remocao = input("O que deseja fazer agora?"
                                            "\na -Remover livro por ano."
                                            "\nb -Remover livro por título"
                                            "\nz -Retornar ao menu anterior\n"
                                            "ESCOLHA: ")

                    if escolha_remocao == "a":
                        remover_livros.rmv_ano(input("Digite o ano limite para remoção dos livros: "))
                        retornar()

                    elif escolha_remocao == "b":
                        remover_livros.rmv_titulo(input("Digite o titulo do livro para remoção: "))
                        retornar()

                    elif escolha_remocao == "z":
                        escolha = escolha_remocao

                    else:
                        print("Opção inválida!")
                        retornar()

                #menu f
                while escolha == "f":
                    print("===============================================")
                    print("     Bem vindo à busca de livros no acervo!     ")
                    print("===============================================")
                    escolha_busca = input("O que deseja fazer agora?"
                                          "\na -Procurar livros no acervo"
                                          "\nz -Retornar ao menu anterior\n"
                                          "ESCOLHA: ")

                    if escolha_busca == "a":
                        busca_dados.busca(input('Digite o tipo da busca: "ano", "titulo", "assunto" ou "autores".'),
                                          input("Digite o termo de busca."))
                        retornar()

                    elif escolha_busca == "z":
                        escolha = escolha_busca

                    else:
                        print("Opção inválida!")
                        retornar()
                #menu g
                while escolha == "g":
                    print("===============================================")
                    print("Bem vindo à locação/reserva de livros do acervo!")
                    print("===============================================")
                    escolha_aluguel = input("O que deseja fazer agora?"
                                            "\na -Alugar um livro."
                                            "\nb -Reservar um livro."
                                            "\nc -Habilitar um livro para reserva."
                                            "\nz -Retornar ao menu anterior\n"
                                            "ESCOLHA: ")

                    if escolha_aluguel == "a":
                        alugar_reservar.alugar(input("Digite o título a ser alugado: "),
                                               input("Digite a data de devolução(dd-mm-aaaa): "),
                                               input("Digite o usuário que irá alugar: "))
                        retornar()

                    elif escolha_aluguel == "b":
                        alugar_reservar.reservar(input("Digite o título a ser reservado: "),
                                                 input("Digite o nome do usuário que irá reservar: "))
                        retornar()

                    elif escolha_aluguel == "c":
                        alugar_reservar.habilitar_reserva(input("Digite o título a ser habilitado: "),
                                                          int(input("Digite a quantidade a ser habilitada: ")))
                        retornar()

                    elif escolha_aluguel == "z":
                        escolha = escolha_aluguel

                    else:
                        print("Opção inválida!")
                        retornar()

                #menu h
                while escolha == "h":
                    print("===============================================")
                    print("     Bem vindo ao menu de status de livro!     ")
                    print("===============================================")
                    escolha_status = input("O que deseja fazer agora?"
                                           "\na -Verificar status de um título."
                                           "\nz -Retornar ao menu anterior\n"
                                           "ESCOLHA: ")

                    if escolha_status == "a":
                        print(status_do_livro.status(input("Digite o título do livro: ")))
                        retornar()

                    elif escolha_status == "z":
                        escolha = escolha_status

                    else:
                        print("Opção inválida!")
                        retornar()

                #menu i
                while escolha == "i":
                    print("===============================================")
                    print("  Bem vindo ao menu de geração de relatórios!  ")
                    print("===============================================")

                    escolha_relatorio = input("O que deseja fazer agora?"
                                              "\na -Gerar relatório de acervo."
                                              "\nb -Gerar relatório de categoria."
                                              "\nc -Gerar relatório de temática."
                                              "\nz -Retornar ao menu anterior\n"
                                              "ESCOLHA: ")

                    if escolha_relatorio == "a":
                        relatorios.rel_acervo()
                        retornar()

                    if escolha_relatorio == "b":
                        relatorios.rel_categoria()
                        retornar()

                    if escolha_relatorio == "c":
                        relatorios.rel_tematica()
                        retornar()

                    if escolha_relatorio == "z":
                        escolha = escolha_relatorio

                #menu j
                while escolha == "j":
                    rodar = False
                    escolha = "y"
                    print("Sistema encerrando operação!")

        else:
            print("Nome de usuário ou senha incorretos, tente novamente.\n")


main()
