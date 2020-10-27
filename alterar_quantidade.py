from saveload import *

#adiciona "quantidade" copias de um livro ja existente
def alt_quant(titulo, quantidade):
    dicionario = carregar()
    if titulo in dicionario["titulo"]:
        temp = dicionario["titulo"].index(titulo)
        for i in range(int(quantidade)):
            for key in dicionario:
                dicionario[key].insert(temp+1, dicionario[key][temp])
        salvar(dicionario)
    else:
        print(f"O livro {titulo} não está no acervo da biblioteca.")


