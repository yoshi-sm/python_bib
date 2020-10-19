from saveload import *

def cadastroCategoriaTematica():

    #Carregar as informações do dicionario
    cadastro = carregar()

    #Adicionando Categoria e/ou temática
    cadastro['Categorias'].append(input('Categoria: '))
    cadastro['Tematicas'].append(input('Tematica: '))

    #salvar o que foi adicionado
    salvar(cadastro)

cadastroCategoriaTematica()