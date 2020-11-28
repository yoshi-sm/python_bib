from saveload import *
from datetime import datetime
from categoria_tematica import obter_categorias, obter_tematicas

# titulo, autores, alugado, data_devolucao

def rel_acervo():
    dicionario = carregar()
    with open(f"relatorios/rel_acervo_{datetime.now().strftime('%d-%m-%Y-%f')}.txt", "w") as f:

        f.write("RELATÓRIO GERAL DA BIBLIOTECA\n")
        for i in range(len(dicionario["titulo"])):
            if dicionario['alugado'][i]:
                dicionario['alugado'][i] = "Sim"
                f.write(f"========================================================================================\n"
                    f"Título: {str(dicionario['titulo'][i])}\n"
                    f"Autores: {str(dicionario['autores'][i])}\n"
                    f"Localização: {dicionario['localizacao'][i]}\n"
                    f"Alugado? {dicionario['alugado'][i]}\n"
                    f"Data de devolução: {dicionario['data_devolucao'][i]}\n")
            else:
                dicionario['alugado'][i] = "Não"
                f.write(f"========================================================================================\n"
                    f"Título: {str(dicionario['titulo'][i])}\n"
                    f"Autores: {str(dicionario['autores'][i])}\n"
                    f"Localização: {dicionario['localizacao'][i]}\n"
                    f"Alugado? {dicionario['alugado'][i]}\n")
        f.write(f"\n\n\nRelatorio gerado em: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

    print("Relatório gerado com sucesso!")

def rel_categoria():
    categorias = obter_categorias()
    with open(f"relatorios/rel_categ_{datetime.now().strftime('%d-%m-%Y-%f')}.txt", "w") as f:
        f.write("RELATÓRIO GERAL DE CATEGORIAS\n"
        "========================================================================================\n")
        for i in categorias:
            f.write(f"Categoria: {i}\n")

            try:
                if categorias[i][0]:
                    f.write("Livros na categoria: ")
                    for j in range(len(categorias[i])):
                        f.write(f" {categorias[i][j]},")
            except:
                f.write("Nenhum título nessa categoria.")

            f.write(f"\n========================================================================================\n")

        f.write(f"\n\n\nRelatorio gerado em: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

    print("Relatório gerado com sucesso!")

def rel_tematica():
    tematicas = obter_tematicas()
    with open(f"relatorios/rel_tematica_{datetime.now().strftime('%d-%m-%Y-%f')}.txt", "w") as f:
        f.write("RELATÓRIO GERAL DE TEMATICAS\n"
        "========================================================================================\n")
        for i in tematicas:
            f.write(f"Tematicas: {i}\n")

            try:
                if tematicas[i][0]:
                    f.write("Livros sobre a tematica: ")
                    for j in range(len(tematicas[i])):
                        f.write(f" {tematicas[i][j]},")
            except:
                f.write("Nenhum título com essa temática.")

            f.write(f"\n========================================================================================\n")

        f.write(f"\n\n\nRelatorio gerado em: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

    print("Relatório gerado com sucesso!")