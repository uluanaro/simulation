from simulation import Simulation
from map import Map
from actions import InitMapAction, MoveCreaturesAction, RenderAction, SpawnGrassAction

map = Map(width=10, height=10)
init_actions = [InitMapAction()]
simulation = Simulation(map, init_actions=init_actions, turn_actions=[])
simulation.turn_actions = [
    MoveCreaturesAction(),
    SpawnGrassAction(),
    RenderAction(simulation)
]
simulation.start_simulation()