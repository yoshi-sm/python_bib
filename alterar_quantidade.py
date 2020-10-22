from saveload import carregar, salvar


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


# """def alt_reserva(titulo, quantidade):
#     dicionario = carregar()
#     if titulo in dicionario["titulo"]:
#         temp = dicionario["titulo"].index(titulo)
#         disponivel = dicionario["unidades"][temp]
#         if quantidade >= disponivel:
#             print("Quantidade digitada é inválida!")
#         else:
#             dicionario["unidades_reserva"][temp] = quantidade
#             salvar(dicionario)
#     else:
#         print(f"O livro {titulo} não está no acervo da biblioteca.")"""