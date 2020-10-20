import funcionarios


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
                                "\nd -Atualizar títulos que podem ser reservados"
                                "\ne -Remover títulos do acervo"
                                "\nf -Busca de livros no acervo"
                                "\ng -Obter status do livro"
                                "\nh -Gerar relátorios"
                                "\ni -Sair do sistema\n")

                if escolha == "a":
                    pass
                elif escolha == "i":
                    rodar = False
                    print("Sistema encerrando operação!")

        else:
            print("Nome de usuário ou senha incorretos, tente novamente.\n")

main()