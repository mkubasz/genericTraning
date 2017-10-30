import datetime
import genetic
from string import ascii_letters


def display(genes, target, startTime):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(genes, target)
    print("{0}\t{1}\t{2}".format(genes, fitness, str(timeDiff)))


def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes) if expected == actual)



def test_Hello_World():
    target = "Hello World!"
    guess_password(target)


def guess_password(target):
    genset = ascii_letters + ' .!'
    startTime = datetime.datetime.now()

    def fnGetFitness(genes):
        return get_fitness(genes, target)
    
    def fnDisplay(genes):
        return display(genes, target, startTime)

    optimalFitness = len(target)
    genetic.get_best(fnGetFitness, 
            len(target),
            optimalFitness,
            genset, 
            fnDisplay)
if __name__ == '__main__':
    test_Hello_World()
