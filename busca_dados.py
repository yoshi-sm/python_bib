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
                print("Livro: ")
                for key in dicionario:
                    print(f"{key}: {dicionario[key][i]}, ", end='')
                print("\n\n")

        else:
            print("Nenhum resultado encontrado!")
    else:
        print("modalidade de busca inválida!")



