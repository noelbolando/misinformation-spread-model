"""
This file contains all the model classes necesssary for the SEHIR model.
"""

import math
import mesa
from mesa import Model
import networkx as nx

from agents import State, MisinformationAgent

"""
Generalized function to find the number of agents for each state
"""
def number_state(model, state):
    return sum(1 for a in model.grid.get_all_cell_contents() if a.state is state)

"""
Specific function to find the number of SUSCEPTIBLE agents
"""
def number_susceptible(model):
    return number_state(model, State.SUSCEPTIBLE)

"""
Specific function to find the number of EXPOSED agents
"""
def number_exposed(model):
    return number_state(model, State.EXPOSED)

"""
Specific function to find the number of HIBERNATORS
"""
def number_hibernators(model):
    return number_state(model, State.HIBERNATORS)

"""
Specific function to find the number of INFECTED agents
"""
def number_infected(model):
    return number_state(model, State.INFECTED)

"""
Specific function to find the number of RESISTANT agents
"""
def number_resistant(model):
    return number_state(model, State.RESISTANT)

class MisinformationNetwork(Model):
    """A misinformation model with some number of agents"""

    """Define the model attributes"""
    def __init__(
            self,
            num_nodes = 10,
            avg_node_degree = 3,

            mu = 0.00325,
            n2 = 0.7985,
            phi = 1,
            b1 = 0.69918,
            b2 = 0.21763,
            b3 = 0.71845,
            b4 = 0.19675,
            b5 = 0.097,
            l2 = 0.299675,
            l3 = 0.23715,
            seed=None
    ):
        super().__init__(seed=seed)
        self.num_nodes = num_nodes
        prob = avg_node_degree / self.num_nodes
        self.G = nx.erdos_renyi_graph(n=self.num_nodes, p=prob)
        self.grid = mesa.space.NetworkGrid(self.G)
