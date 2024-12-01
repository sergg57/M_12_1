import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        Afina_walker = Runner("Afina")
        for i in range(10):
            Afina_walker.walk()
        self.assertEqual(Afina_walker.distance, 50)

    def test_run(self):
        Platon_runner = Runner("Platon")
        for i in range(10):
            Platon_runner.run()
        self.assertEqual(Platon_runner.distance, 100)

    def test_challenge(self):
        Afina_runner = Runner("Afina")
        Platon_walker = Runner("Platon")
        for i in range(10):
            Afina_runner.run()
            Platon_walker.walk()
        distance_1 = Afina_runner.distance
        distance_2 = Platon_walker.distance
        print(f'Дистанции не равны: {distance_1} {distance_2}')
        self.assertNotEqual(distance_1, distance_2)


if __name__ == '__main__':
    unittest.main()