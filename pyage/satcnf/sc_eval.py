import random
import time
from pyage.core.operator import Operator
from sc_genotype import CNFGenotype


class SATEvaluation(Operator):
    def __init__(self, cnf_form):
        super(SATEvaluation, self).__init__(CNFGenotype)
        self.cnf_form = cnf_form

    def process(self, population):
        for genotype in population:
            genotype.fitness = self.evaluate(genotype)

    def evaluate(self, genotype):
        evaluated = 0.0

        for group in self.cnf_form:
            # group_hits = 0
            for expected_val, index in group:
                if expected_val == genotype.values[index]:
                    # group_hits += 1
                    evaluated += 1
                    break
            # evaluated += float(group_hits) / len(group)

        return evaluated
