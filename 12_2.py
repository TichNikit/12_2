import A12
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.Usain = A12.Runner('Usain', 10)
        self.Andrey = A12.Runner('Andrey', 9)
        self.Nik = A12.Runner('Nik', 3)



    def test_Tournament_all(self):
        turna = A12.Tournament(90, self.Usain, self.Andrey, self.Nik)
        self.all_results = turna.start()
        self.assertEqual(self.all_results[len(self.all_results)].name, 'Nik')

    def test_Tournament_Usain_and_Nik(self):
        turna = A12.Tournament(90, self.Usain, self.Nik)
        self.all_results = turna.start()
        self.assertEqual(self.all_results[len(self.all_results)].name, 'Nik')

    def test_Tournament_Annrey_and_Nik(self):
        turna = A12.Tournament(90, self.Andrey, self.Nik)
        self.all_results = turna.start()
        self.assertEqual(self.all_results[len(self.all_results)].name, 'Nik')

    @classmethod
    def tearDownClass(self):
        print(*self.all_results, sep='\n')





    '''def test_walk(self):
        nik = A12_1.Runner('Nik')
        for _ in range(10):
            nik.walk()
        self.assertEqual(nik.distance, 50)

    def test_walk(self):
        nikita = A12_1.Runner('Nikita')
        for _ in range(10):
            nikita.run()
        self.assertEqual(nikita.distance, 100)

    def test_challenge(self):
        niki = A12_1.Runner('Niki')
        ta = A12_1.Runner('Ta')
        for _ in range(10):
            niki.walk()
            ta.run()
        self.assertEqual((niki.distance,ta.distance), (50,100))'''