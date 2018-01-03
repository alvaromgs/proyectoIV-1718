import time
import shelve

def getLists():
    lists = shelve.open('lists.db')
    pelis = {}
    for k,v in lists.items():
        pelis[k] = v
    lists.close()

    return pelis

def getList(lista):
    # if list in pelis:
    #     print(list)
    #     for k, v in pelis[list][0].items():
    #         print(k, "\t", v)
    #     print ("")
    # else:
    #     print ("No existe esa lista\n")
    lists = shelve.open('lists.db')

    if lista in lists:
        l = lists[lista]
        lists.close()
        return l
    else:
        lists.close()
        return False

def addList(name):
    lists = shelve.open('lists.db')
    lists[name] = [{}, time.strftime("%d/%m/%Y %H:%M")]
    lists.close()

def renameList(lista, newname):
    lists = shelve.open('lists.db')
    if lista in lists:
        lists[newname] = lists[lista]
        del lists[lista]
        lists.close()
        updateTime(newname)
    else:
        lists.close()
        return False

def removeList(lista):
    lists = shelve.open('lists.db')
    if lista in lists:
        del lists[lista]
        lists.close()
    else:
        lists.close()
        return False

def getMovies(lista):
    lists = shelve.open('lists.db')
    if lista in lists:
        pelis = lists[lista][0]
        lists.close()
        return pelis
    else:
        lists.close()
        return False

def getRating(lista, peli):
    lists = shelve.open('lists.db')
    if lista in lists:
        peli = lists[lista][0][peli]
        lists.close()
        return peli
    else:
        lists.close()
        return False

def getTime(lista):
    lists = shelve.open('lists.db')
    if lista in lists:
        time = lists[lista][1]
        lists.close()
        return time
    else:
        lists.close()
        return False

def updateMovie(lista, peli, nota):
    lists = shelve.open('lists.db')
    if lista in lists:
        lists[lista][0][peli] = nota
        lists.close()
        updateTime(lista)
    else:
        lists.close()
        return False

def updateTime(lista):
    lists = shelve.open('lists.db')
    lists[lista][1] = time.strftime("%d/%m/%Y %H:%M")
    lists.close()

def removeMovie(lista, peli):
    lists = shelve.open('lists.db')
    if lista in lists:
        del lists[lista][0][peli]
        lists.close()
        updateTime(lista)
    else:
        lists.close()
        return False
