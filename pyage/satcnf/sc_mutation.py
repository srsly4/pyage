import logging
import random
from pyage.core.operator import Operator
from sc_genotype import CNFGenotype

logger = logging.getLogger(__name__)


class AbstractMutation(Operator):
    def __init__(self, type, probability):
        super(AbstractMutation, self).__init__()
        self.probability = probability

    def process(self, population):
        for genotype in population:
            if random.random() < self.probability:
                self.mutate(genotype)


class Mutation(AbstractMutation):
    def __init__(self, probability, evol_probability):
        super(Mutation, self).__init__(CNFGenotype, evol_probability)
        self.probability = probability
        self.evol_probability = evol_probability

    def mutate(self, genotype):
        logger.debug("Mutating genotype: {0}".format(genotype))
        for key in xrange(0, len(genotype.values)):
            rand = random.random()
            if rand < self.evol_probability:
                genotype.values[key] = 1 - genotype.values[key]


class ShiftMutation(AbstractMutation):
    def __init__(self, probability):
        super(ShiftMutation, self).__init__(CNFGenotype, probability)
        self.probability = probability

    def mutate(self, genotype):
        logger.debug("Mutating genotype: {0}".format(genotype))
        old_values = list(genotype.values)
        for key in xrange(0, len(genotype.values)):
            genotype.values[key] = old_values[(key+1) % len(genotype.values)]
