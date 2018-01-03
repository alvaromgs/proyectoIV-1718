import unittest
import time
from listas import *

class myTest(unittest.TestCase):

    def testgetLists(self):
        self.assertTrue(getLists(), "La lista está vacía")

    def testgetList(self):
        self.assertIsInstance(getList("Vistas"), list, "No es una lista")

    def testaddList(self):
        addList("Nolan")
        self.assertTrue("Nolan" in getLists(), "No se ha añadido la lista")

    def testrenameList(self):
        renameList("Pendientes", "Pendientesv2")
        self.assertTrue("Pendientesv2" in getLists(), "No se ha renombrado la lista")

    def testremoveList(self):
        removeList("Favoritas")
        self.assertTrue("Favoritas" not in getLists(), "No se ha borrado la lista")

    def testgetMovies(self):
        self.assertIsInstance(getMovies("Vistas"), dict, "No es un diccionario")

    def testgetRating(self):
        self.assertIsInstance(getRating("Vistas", "Cadena perpetua"), (int, float), "No es un número")

    def testgetTime(self):
        self.assertIsInstance(getTime("Vistas"), str, "No es un string")

    def testupdateMovie(self):
        nota = 9
        updateMovie("Vistas", "Cadena perpetua", nota)
        updateMovie("Vistas", "El truco final", nota)
        self.assertTrue(getRating("Vistas", "Cadena perpetua") == nota, "No se ha actualizado la puntuación")
        self.assertTrue("El truco final" in getMovies("Vistas"), "No se ha añadido la película")

    def testupdateTime(self):
        updateTime("Vistas")
        self.assertTrue(getTime("Vistas") == time.strftime("%d/%m/%Y %H:%M"), "No se ha actualizado la fecha de modificación de la lista")

    def testremoveMovie(self):
        removeMovie("Vistas", "Cadena perpetua")
        self.assertTrue("Cadena perpetua" not in getMovies("Vistas"), "No se ha borrado la película")

if __name__ == '__main__':
    unittest.main()
