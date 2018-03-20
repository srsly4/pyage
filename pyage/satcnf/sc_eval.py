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
        all_literals = 0
        all_hits = 0.0
        for group in self.cnf_form:
            group_hits = 0
            for expected_val, index in group:
                all_literals += 1
                if expected_val == genotype.values[index]:  # that's an OR clausule hit
                    group_hits += 1
                    all_hits += 1
            if group_hits > 0:
                evaluated += 1

        evaluated += float(all_hits) / float(all_literals)
        evaluated += random.random() * 0.01
        return evaluated
