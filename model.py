"""
This file contains all the model classes necesssary for the SEHIR model.
"""

import math
import mesa
from mesa import Model
import networkx as nx

from agents import State, MisinformationAgent

# Generalized function to find the number of agents in each state
def number_state(model, state):
    """Generalized Agent State counting function."""
    return sum(1 for a in model.grid.get_all_cell_contents() if a.state is state)

# Specific function to find the number of SUSCEPTIBLE agents
def number_susceptible(model):
    """Find the number of susceptible agents."""
    return number_state(model, State.SUSCEPTIBLE)

# Specific function to find the number of EXPOSED agents
def number_exposed(model):
    """Find the number of exposed agents."""
    return number_state(model, State.EXPOSED)

# Specific function to find the number of HIBERNATORS
def number_hibernators(model):
    """Find the number of hibernating agents."""
    return number_state(model, State.HIBERNATORS)

# Specific function to find the number of INFECTED agents
def number_infected(model):
    """Find the number of infected agents."""
    return number_state(model, State.INFECTED)

# Specific function to find the number of RESISTANT agents
def number_resistant(model):
    "Find the number of resistant agents."
    return number_state(model, State.RESISTANT)

class MisinformationNetwork(Model):
    """A misinformation model with some number of agents"""

    # Define the model attributes
    def __init__(
            self,
            num_nodes = 10,
            avg_node_degree = 3,
            virus_check_frequency=0.4,
            initial_outbreak_size=1,
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
            seed=None,
    ):
        super().__init__(seed=seed)
        self.num_nodes = num_nodes
        prob = avg_node_degree / self.num_nodes
        self.G = nx.erdos_renyi_graph(n=self.num_nodes, p=prob)
        self.grid = mesa.space.NetworkGrid(self.G)

        self.initial_outbreak_size = (initial_outbreak_size if initial_outbreak_size <= num_nodes else num_nodes)

        self.mu = mu
        self.n2 = n2
        self.phi = phi
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3 
        self.b4 = b4
        self.b5 = b5
        self.l2 = l2
        self.l3 = l3
        self.virus_check_frequency = virus_check_frequency

        self.datacollector = mesa.DataCollector(
            {
                "Infected": number_infected,
                "Susceptible": number_susceptible,
                "Resistant": number_resistant,
                "Exposed": number_exposed,
                "Hibernators": number_hibernators
            }
        )

        # Create Susceptible agents
        for node in self.G.nodes():
            a = MisinformationAgent(
                self,
                State.SUSCEPTIBLE,
                self.mu,
                self.n2,
                self.phi,
                self.b1,
                self.b2,
                self.b3,
                self.b4,
                self.b5,
                self.l2,
                self.l3,
                self.virus_check_frequency 
            )

            # Add the susceptible agents to the node
            self.grid.place_agent(a, node)

        # Infect some of the agents added to the node
        infected_nodes = self.random.sample(list(self.G), self.initial_outbreak_size)
        # Randomly infect some of the agents based on the initial_outbreak_size
        for a in self.grid.get_cell_list_contents(infected_nodes):
            a.state = State.INFECTED

        # Expose some of the agents added to the node
        exposed_nodes = self.random.sample(list(self.G))
        # Randomly expose some of the agents
        for a in self.grid.get_cell_list_contents(exposed_nodes):
            a.state = State.EXPOSED

        # Hibernate some of the agents added to the node
        hibernating_nodes = self.random.sample(list(self.G))
        # Randomly hibernate some of the agents
        for a in self.grid.get_cell_list_contents(hibernating_nodes):
            a.state = State.HIBERNATORS

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        """Call the agent steps"""
        self.agents.shuffle_do("step")
        # Collect data throughout the steps
        self.datacollector.collect(self)
