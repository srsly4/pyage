
class Cities(object):
    def __init__(self, cities):
        self.cities = [list(h) for h in cities]
        self.fitness = None

    def __str__(self):
        return "{0}\nfitness: {1}".format("\n".join(map(str,self.votes)), self.fitness)
        
