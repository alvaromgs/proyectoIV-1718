import time

pelis = {
            "Favoritas": [
            {"Blade Runner": 7, "Pulp Fiction": 8},
            time.strftime("%d/%m/%Y %H:%M")
            ]
        ,
            "Pendientes": [
            {"El padrino": 9, "Uno de los nuestros": 10},
            time.strftime("%d/%m/%Y %H:%M")
            ]
        }

pelis["Vistas"] =   [
                        {"Cadena perpetua": 7, "El caballero oscuro": 8},
                        time.strftime("%d/%m/%Y %H:%M")
                    ]

def getLists():
    return pelis

def getList(lista):
    # if list in pelis:
    #     print(list)
    #     for k, v in pelis[list][0].items():
    #         print(k, "\t", v)
    #     print ("")
    # else:
    #     print ("No existe esa lista\n")

    if lista in pelis:
        return pelis[lista]
    else:
        return False

def addList(name):
    pelis[name] = [{}, time.strftime("%d/%m/%Y %H:%M")]

def renameList(lista, newname):
    if lista in pelis:
        pelis[newname] = pelis.pop(lista)
        updateTime(newname)
    else:
        return False

def removeList(lista):
    if lista in pelis:
        del pelis[lista]
        return True
    else:
        return False

def getMovies(lista):
    if lista in pelis:
        return pelis[lista][0]
    else:
        return False

def getRating(lista, peli):
    if lista in pelis:
        return pelis[lista][0][peli]
    else:
        return False

def getTime(lista):
    if lista in pelis:
        return pelis[lista][1]
    else:
        return False

def updateMovie(lista, peli, nota):
    if lista in pelis:
        pelis[lista][0][peli] = nota
        updateTime(lista)
        return True
    else:
        return False

def updateTime(lista):
    pelis[lista][1] = time.strftime("%d/%m/%Y %H:%M")

def removeMovie(lista, peli):
    if lista in pelis:
        del pelis[lista][0][peli]
        updateTime(lista)
        return True
    else:
        return False
