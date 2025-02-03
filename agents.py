"""
This file contains all the agent classes necesssary for the SEHIR model.
"""

from enum import Enum
from mesa import Agent

class State(Enum):
    """Define the initial states of the agents."""
    SUSCEPTIBLE = 0
    EXPOSED = 1
    HIBERNATORS = 2
    INFECTED = 3
    RESISTANT = 4

class MisinformationAgent(Agent):
    """Individual misinformation-spreading agents."""

    def __init__(
            self,
            model,
            initial_state,
            
            virus_check_frequency, # check the status of infected agents
            mu, # the rate of deactivation for users
            n2, # misinformation transmission coefficient
            phi, # when phi=0, there will be no misinforamtion, when phi=1 agent will spread disinformation
            b1, # transimission rate from H -> I
            b2, # transmission rate from E -> H
            b3, # transmission rate from E -> I
            b4, # recovery rate from S -> R
            b5, # recovery rate from E -> R
            l2, # recovery rate from H -> R
            l3, # recovery rate from I -> R
    ):
        super().__init__(model)

        # Define the initial state of all agents
        self.state = initial_state

        # Define the properties of the agents
        self.virus_check_frequency = virus_check_frequency
        self.n2 = n2
        self.phi = phi
        self.mu = mu
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.l2 = l2
        self.l3 = l3
    
    """
    General function for exploring the local neighborhood
    """
    def neighborhood_explorer(self):
        neighbors_nodes = self.model.grid.get_neighborhood(
            self.pos, include_center=False
        )
        return neighbors_nodes

    """
    Function defining how SUSCEPTIBLE agents evolve
    These agents can become EXPOSED or RESISTANT based on phi value
    If phi=0, S->R; if phi=1, S->E
    """
    def determine_if_susceptible_agents_become_exposed(self, neighbors_nodes):
        # Find the SUSCEPTIBLE agents
        susceptible_neighbors = [
            agent
            for agent in self.model.grid.get_cell_list_contents(neighbors_nodes)
            if agent.state is State.SUSCEPTIBLE
        ]
        for a in susceptible_neighbors:
            if self.random.random < self.phi():
                a.state = State.RESISTANT
            else:
                a.state = State.EXPOSED
         
    """
    Function defining how EXPOSED agents evolve
    These agents can be become HIBERNATORS, INFECTED, or RESISTANT
    """
    def exposed_agents_evolve(self, neighbors_nodes):
        # Find the EXPOSED agents
        exposed_neighbors = [
            agent
            for agent in self.model.grid.get_cell_list_contents(neighbors_nodes)
            if agent.state is State.SUSCEPTIBLE
        ]
        for a in exposed_neighbors:
            if self.random.random() < self.b2:
                a.state = State.HIBERNATORS
            if self.random.random () < self.b3:
                a.state = State.INFECTED
            elif self.random.random() < self.b5:
                a.state = State.RESISTANT

    """
    Function defining how HIBERNATORS evolve
    These agents can become INFECTED or RESISTANT
    """
    def hibernators_evolve(self, neighbors_nodes):
        # Find the HIBERNATORS
        hibernators_neighbors = [
            agent
            for agent in self.model.grid.get_cell_list_contents(neighbors_nodes)
            if agent.state is State.HIBERNATORS
        ] 
        for a in hibernators_neighbors:
            if self.random.random() < self.b1:
                a.state = State.INFECTED
            elif self.random.random() < self.l2:
                a.state = State.RESISTANT
    
    """
    Function defining how INFECTED agents become RESISTANT
    """
    def infected_agents_evolve(self, neighbors_nodes):
        # Find the HIBERNATORS
        infected_neighbors = [
            agent
            for agent in self.model.grid.get_cell_list_contents(neighbors_nodes)
            if agent.state is State.INFECTED
        ]
        for a in infected_neighbors:
            if self.random.random() <= self.l1:
                self.state = State.RESISTANT
    
    """
    Define the steps for agents within the model
    """
    def step(self):
        if self.state is State.SUSCEPTIBLE:
            self.determine_if_susceptible_agents_become_exposed()
        if self.state is State.EXPOSED:
            self.exposed_agents_evolve()
        if self.state is State.HIBERNATORS:
            self.hibernators_evolve()
        if self.state is State.INFECTED:
            self.infected_agents_evolve()
 