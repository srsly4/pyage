import random
from pyage.core.emas import EmasAgent
from pyage.core.operator import Operator
from pyage.core.inject import Inject
from sc_genotype import CNFGenotype
import random


class EmasInitializer(object):
    def __init__(self, values, energy, size):
        self.values = values
        self.energy = energy
        self.size = size

    @Inject("naming_service")
    def __call__(self):
        agents = {}
        for value in self.values:
            agent = EmasAgent(CNFGenotype(value), self.energy, self.naming_service.get_next_agent())
            agents[agent.get_address()] = agent
        return agents


def root_agents_factory(count, type):
    def factory():
        agents = {}
        for i in range(count):
            agent = type('R' + str(i))
            agents[agent.get_address()] = agent
        return agents

    return factory


class SATCNFInitializer(Operator):
    def process(self, population):
        values = self.__call__()
        for i in xrange(len(values)):
            population.append(CNFGenotype(values[i]))

    def __init__(self, values_nr, count, seed):
        self.values_nr = values_nr
        self.count = count
        self.required_type = None
        random.seed(seed)

    def __call__(self):
        values = []
        for _ in xrange(self.count):
            val_set = []
            for __ in xrange(self.values_nr):
                val_set.append(1 if random.random() < 0.5 else 0)
            values.append(val_set)

        random.seed()
        return values
