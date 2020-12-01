from saveload import *


# adiciona "quantidade" copias de um livro ja existente
def alt_quant(titulo, quantidade):
    dicionario = carregar()
    if titulo in dicionario["titulo"]:
        temp = dicionario["titulo"].index(titulo)
        for i in range(int(quantidade)):
            dicionario["titulo"].insert(temp+1, dicionario["titulo"][temp])
            dicionario["autores"].insert(temp+1, dicionario["autores"][temp])
            dicionario["assunto"].insert(temp + 1, dicionario["assunto"][temp])
            dicionario["ano"].insert(temp + 1, dicionario["ano"][temp])
            dicionario["localizacao"].insert(temp + 1, dicionario["localizacao"][temp])
            dicionario["data_devolucao"].insert(temp + 1, "")
            dicionario["alugado"].insert(temp + 1, False)
            dicionario["usuario_reserva"].insert(temp + 1, "")
            dicionario["usuario_aluguel"].insert(temp + 1, "")
            dicionario["reserva"].insert(temp + 1, False)
        salvar(dicionario)
    else:
        print(f"O livro {titulo} não está no acervo da biblioteca.")


