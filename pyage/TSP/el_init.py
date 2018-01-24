import numpy
from pyage.core.emas import EmasAgent
from pyage.core.inject import Inject
from pyage.TSP.el_genotype import Cities
import random
from random import uniform

class EmasInitializer(object):

    def __init__(self, cities, energy, size):
        self.cities = cities
        self.energy = energy
        self.size = size

    @Inject("naming_service")
    def __call__(self):
        agents = {}
        for i in range(self.size):
            agent = EmasAgent(Cities(self.cities), self.energy, self.naming_service.get_next_agent())
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

class CitiesInitializer(object):

    def __init__(self, cities_nr, seed):
        self.cities_nr = cities_nr
        random.seed(seed)

    def __call__(self):
        cities = numpy.zeros((self.cities_nr, 2))
        for i in range(self.cities_nr):
            cities[i][0] = uniform(0, 10)
            cities[i][1] = uniform(0, 10)
        random.seed()
        return cities