# coding=utf-8
import logging
import os
import math

from pyage.core import address
from pyage.core.agent.agent import generate_agents, Agent

from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition

from sc_init import EmasInitializer, SATCNFInitializer, root_agents_factory
from sc_mutation import Mutation
from sc_crossover import Crossover
from sc_selection import TournamentSelection
from sc_eval import SATEvaluation
from naming_service import NamingService
from cnf_loader import load_values

logger = logging.getLogger(__name__)

# cnf = [
#     [(0, 0), (1, 2)],  # ~a || c
#     [(0, 0), (1, 2), (0, 4)],  # ~a || c || ~e
#     [(0, 1), (1, 2), (1, 3), (0, 4)],  # ~b || c || d || ~e
#     [(1, 0), (0, 1), (1, 2)],  # a || ~b || c
#     [(0, 4), (1, 5)],
# ]
# variables = 6
# clauses = 5
# values_nr = 6

cnf, variables, clauses = load_values("data3.cnf")

# init_values = SATCNFInitializer(variables, 10, 'nopeland')()
#
# logger.info("Initial values:\n%s", "\n".join(map(str, cnf)))


agents_count = 2
# logger.debug("EMAS, %s agents", agents_count)
# agents = root_agents_factory(agents_count, AggregateAgent)
agents = generate_agents("agent", agents_count, Agent)

stop_condition = lambda: StepLimitStopCondition(10000)

operators = lambda: [SATEvaluation(cnf), TournamentSelection(size=20, tournament_size=20),
                     Crossover(size=40),
                     Mutation(probability=0.2, evol_probability=0.75)]
initializer = lambda: SATCNFInitializer(variables, 250, 'wrt')


def simple_cost_func(x): return abs(x)*10

address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatistics('fitness_satcnf_%s_pyage.txt' % __name__)

naming_service = lambda: NamingService(starting_number=2)
