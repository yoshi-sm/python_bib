import json
#funcoes para mexer no bd de funcionarios, não utilizados no main(), exceto o login
bd_func = "bd/funcionarios.dat"


def reset_funcionarios():
    with open(bd_func, "w") as f:
        f.write("{'usuario' : [] , 'senha' : []}")


def cadastro_func(usuario, senha):
    cadastrar = True
    with open(bd_func, "r") as f:
        dicionario = json.loads(f.readline())
        if dicionario["usuario"].count(usuario) != 0:
            print("Usuario já existe!")
            cadastrar = False
        else:
            dicionario["usuario"].append(usuario)
            dicionario["senha"].append(senha)

    if cadastrar:
        with open(bd_func, "w") as f:
            f.write(json.dumps(dicionario))


#usado para auteticar o login no começo do main
def login_func(login, senha):
    loggado = False
    with open(bd_func) as f:
        dicionario = json.loads(f.readline())
        for i in range(len(dicionario["usuario"])):
            if dicionario["usuario"][i] == login and dicionario["senha"][i] == senha:
                loggado = True

    if loggado:
        return True
    else:
        return False
