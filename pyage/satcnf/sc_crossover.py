import random
from pyage.core.operator import Operator
from sc_genotype import CNFGenotype

import logging

logger = logging.getLogger(__name__)


class AbstractCrossover(Operator):
    def __init__(self, type, size):
        super(AbstractCrossover, self).__init__(type)
        self.__size = size

    def process(self, population):
        parents = list(population)
        for i in range(len(population), self.__size):
            p1, p2 = random.sample(parents, 2)
            genotype = self.cross(p1, p2)
            population.append(genotype)


class Crossover(AbstractCrossover):
    def __init__(self, size):
        super(Crossover, self).__init__(CNFGenotype, size)

    def cross(self, p1, p2):
        # logger.debug("Crossing:\n{0}\nAND\n{1}".format(p1, p2))
        new_values = []
        curr_ndx = 0
        while curr_ndx < len(p1.values):
            # new_values.append(p1.values[curr_ndx] if random.random() < 0.5 else p2.values[curr_ndx])
            new_values.append(p1.values[curr_ndx]*p2.values[curr_ndx] if random.random() < 0.5 else min(1, p1.values[curr_ndx]+p2.values[curr_ndx]))
            curr_ndx += 1

        return CNFGenotype(new_values)
