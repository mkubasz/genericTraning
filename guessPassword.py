import datetime
import genetic
import unittest
from string import ascii_letters


def display(genes, target, start_time):
    time_diff = datetime.datetime.now() - start_time
    fitness = get_fitness(genes, target)
    print("{0}\t{1}\t{2}".format(genes, fitness, str(time_diff)))


def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes) if expected == actual)


def test_Hello_World():
    target = "Hello World!"
    guess_password(target)


def guess_password(target):
    genset = ascii_letters + ' .!'
    start_time = datetime.datetime.now()

    def fnGetFitness(genes):
        return get_fitness(genes, target)

    def fnDisplay(genes):
        return display(genes, target, start_time)

    optimalFitness = len(target)
    genetic.get_best(fnGetFitness,
                     len(target),
                     optimalFitness,
                     genset,
                     fnDisplay)


class GuessPasswordTests(unittest.TestCase):
    def test_Hello_World(self):
        target = "Hello World!"
        self.guess_password(target)

    def guess_password(self, target):
        geneset = ascii_letters + ' .!'
        start_time = datetime.datetime.now()

        def fnGetFitness(genes):
            return get_fitness(genes, target)

        def fnDisplay(genes):
            return display(genes, target, start_time)

        optimal_fitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimal_fitness,
                                geneset, fnDisplay)
        self.assertEqual(best, target)


if __name__ == '__main__':
    unittest.main()
