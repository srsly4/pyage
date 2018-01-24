import logging
import random
from pyage.core.operator import Operator
from pyage.TSP.el_genotype import Cities

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
        super(Mutation, self).__init__(Cities, evol_probability)
        self.probability = probability

    def mutate(self, genotype):
        logger.debug("Mutating genotype: {0}".format(genotype))
        for city in genotype.cities:
            rand = random.random()
            index_of_city = city.index(genotype.candidate)
            if rand < self.probability:
                bias = random.randint(-10,10)
                biased = (index_of_city-bias)%len(city)
                city.insert(biased, city.pop(index_of_city))

				
		


