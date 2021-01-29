import unittest
from sudoku import Sudoku


class claseTest(unittest.TestCase):

    def setUp(self):
        self.instancia_uno  = Sudoku("864371259325849761971265843436192587198657432257483916689734125713528694542916378")
        self.instancia_dos  = Sudoku("346179258187523964529648371965832417472916835813754629798261543631485792254397186")

    def tearDonw(self):
        pass

    def testVerificar_uno(self):
        self.assertEqual(True, self.instancia_uno.getVerificarFila() and self.instancia_uno.getVerificarColumna())

    def testOrdenDos_dos(self):
        self.assertEqual(True, self.instancia_dos.getVerificarFila() and self.instancia_dos.getVerificarColumna())

if __name__ == "__main__":
    unittest.main()
