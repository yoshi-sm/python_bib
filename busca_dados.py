from saveload import *

#retorna os indices do dicionario compativeis com a busca
def busca(tipo, valor):
    dicionario = carregar()
    temp_index = []
    if tipo in dicionario.keys():
        for i in range(len(dicionario[tipo])):
            if dicionario[tipo][i] == valor:
                temp_index.append(i)

    else:
        print("modalidade de busca inválida!")

    return temp_index

#print dos livros de acordo com indices existentes em "lista"
def print_livro(lista, dicionario):
    for i in lista:
        print("\n")
        for key in dicionario:
            print(dicionario[key][i], end=' ')
