from saveload import *

#retorna os indices do dicionario compativeis com a busca
def busca(tipo, valor):
    dicionario = carregar()
    temp_index = []
    tipos_possiveis = ["ano", "titulo", "autores", "assunto"]
    if tipo in tipos_possiveis:
        if valor in dicionario[tipo]:
            for i in range(len(dicionario[tipo])):
                if dicionario[tipo][i] == valor:
                    temp_index.append(i)
            for i in temp_index:
                print("\n\n")
                for key in dicionario:
                    print(f"{dicionario[key]}: {dicionario[key][i]}\n")
        else:
            print("Nenhum resultado encontrado!")
    else:
        print("modalidade de busca inválida!")



#print dos livros de acordo com indices existentes em "lista"
"""def print_livro(lista, dicionario):
    for i in lista:
        print("\n\n")
        for key in dicionario:
            print(f"{dicionario[key]}: {dicionario[key][i]}\n")"""
