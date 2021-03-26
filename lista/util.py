from .models import Item

listafinal = []

def getItem():
    return Item.objects.all()


def arrumalista(lista):
    itens = []
    valores = []
    
    arrumalista = lista.split(',')
    cont = 0
    for palavra in arrumalista:

        if (cont % 2) == 0:
            itens.append(palavra)
        else:
            valores.append(float(palavra))
        cont += 1

    for item, valor in zip(itens, valores):
        listafinal.append([item, valor])

def pega_lista():
    return listafinal


    