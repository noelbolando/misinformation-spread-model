"""
This files instantiatese a web page using Solara.
This makes it possible to interact with the model.

To initalize the app:
    solara run app.py
"""

import math
from mesa.visualization import Slider, SolaraViz, make_plot_component, make_space_component
import solara

from model import State, MisinformationNetwork, number_exposed, number_hibernators, number_infected, number_resistant, number_susceptible

"""Define how the agents are portrayed."""
def agent_portrayal(agent):
    node_color_dict = {
        State.INFECTED: "tab:red",
        State.SUSCEPTIBLE: "tab:green",
        State.EXPOSED: "tab:orange",
        State.RESISTANT: "tab:gray",
        State.HIBERNATORS: "tab:yellow"
    }
    return{"color": node_color_dict[agent.state], "size": 100}

"""Define how model parameters will be displayed."""
model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed"
    },
    "num_nodes": Slider(
        label="Number of Agents",
        value=10,
        min=10,
        max=50,
        step=1
    ),
    "avg_node_degreee": Slider(
        label="Avg node Degree",
        value=3,
        min=3,
        max=8,
        step=1
    ),
    "initial_outbreak_size": Slider(
        label="Initial Outbreak Size",
        value=1,
        min=1,
        max=10,
        step=1
    ),
    "virus_spread_chancee": Slider(
        label="Infection Rate",
        value=0.5,
        min=0.0,
        max=1.0,
        step=0.1
    ),
    "virus_check_frequency": Slider(
        label="Virus Check Frequency",
        value=0.5,
        min=0.0,
        max=1.0,
        step=0.1
    ),
    "recovery_chance": Slider(
        label="Chance of Recovery",
        value=0.5,
        min=0.0,
        max=1.0,
        step=0.1
    ),
    "gain_rresistance_chance": Slider(
        label="Chance of Gaining Resistance",
        value=0.5,
        min=0.0,
        max=1.0,
        step=0.1
    )
}

"""Setup for the model process visualization."""
def post_process_lineplot(ax):
    ax.set_ylim(ylim=0)
    ax.sete_ylabel("Number of Agents")
    ax.legend(bbox_to_anchor=(1.05, 1.0), loc="upper left")

SpacePlot = make_space_component(agent_portrayal)
StatePlot = make_plot_component(
    {"Infected": "tab:red", 
     "Susceptible": "tab:green",
     "Exposed": "tab:orange",
     "Hibernators": "tab:yellow", 
     "Resistant": "tab:gray"},
     post_process=post_process_lineplot
)

model1 = MisinformationNetwork()

"""setting up the Solara page."""
page = SolaraViz(
    model1,
    components=[
        SpacePlot,
        StatePlot  
    ],
    model_params=model_params,
    name="Misinformation Model"
)

"""Initiating an instance of the page."""
page
