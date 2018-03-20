# coding=utf-8
import logging
import os
import math

from pyage.core import address

from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition

from sc_init import EmasInitializer, SATCNFInitializer, root_agents_factory
from sc_mutation import Mutation, ShiftMutation
from sc_crossover import Crossover
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
# values_nr = 6

cnf, variables, clauses = load_values("data_large.cnf")

init_values = SATCNFInitializer(variables, 40, 'amazon')()

logger.info("Initial values:\n%s", "\n".join(map(str, init_values)))


agents_count = 2
logger.debug("EMAS, %s agents", agents_count)
agents = root_agents_factory(agents_count, AggregateAgent)

stop_condition = lambda: StepLimitStopCondition(8000)

agg_size = 50
aggregated_agents = EmasInitializer(values=init_values, size=agg_size, energy=60)

emas = EmasService

minimal_energy = lambda: 10
reproduction_minimum = lambda: 100
migration_minimum = lambda: 120
newborn_energy = lambda: 100
transferred_energy = lambda: 40

budget = 0


def simple_cost_func(x): return abs(x)*10

evaluation = lambda: SATEvaluation(cnf)
crossover = lambda: Crossover(size=20)
mutation = lambda: ShiftMutation(probability=0.02)

address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatistics('fitness_satcnf_%s_pyage.txt' % __name__)

naming_service = lambda: NamingService(starting_number=2)
