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

if __name__ == '__main__':
    unittest.main()
