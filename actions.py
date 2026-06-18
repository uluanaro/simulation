from abc import ABC, abstractmethod
import random
from entities import Herbivore, Predator, Grass, Rock, Tree


class Action(ABC):

    @abstractmethod
    def execute(self, map):
        pass

class PrintMapAction(Action):
    def execute(self, map):
        result = len(map.get_all_entities())
        print(result)

class MoveCreaturesAction(Action):
    def execute(self, map):
        creatures = map.get_all_entities()
        for creature in creatures:
            creature.make_move(map)

class InitMapAction(Action):
    def execute(self, map):
        all_positions = [(x, y) for x in range(map.width) for y in range(map.height)]
        random.shuffle(all_positions)

        herbivore_count = 5
        predator_count = 2
        grass_count = 10
        rock_count = 5
        tree_count = 5

        total = herbivore_count + predator_count + grass_count + rock_count + tree_count
        positions = all_positions[:total]

        i = 0
        for _ in range(herbivore_count):
            x, y = positions[i]
            i += 1
            map.add_entity(Herbivore(x, y, hp=10, speed=1))

        for _ in range(predator_count):
            x, y = positions[i]
            i+=1
            map.add_entity(Predator(x, y, hp=15, speed=1, attack_power=5))

        for _ in range(grass_count):
            x, y = positions[i]
            i+=1
            map.add_entity(Grass(x, y))

        for _ in range(rock_count):
            x, y = positions[i]
            i+=1
            map.add_entity(Rock(x, y))

        for _ in range(tree_count):
            x, y = positions[i]
            i+=1
            map.add_entity(Tree(x, y))

class RenderAction(Action):

    def __init__(self, simulation):
        self.simulation = simulation

    def execute(self, map):
        for y in range(map.height):
            row = []
            for x in range(map.width):
                entity = map.get_entity_at(x, y)
                if entity is None:
                    row.append(".")
                elif isinstance(entity, Herbivore):
                    row.append("H")
                elif isinstance(entity, Predator):
                    row.append("P")
                elif isinstance(entity, Grass):
                    row.append("G")
                elif isinstance(entity, Rock):
                    row.append("R")
                elif isinstance(entity, Tree):
                    row.append("T")
            print(" ".join(row))
        print(f"Ход: {self.simulation.turn_count}")
        print("-" * map.width * 2)

class SpawnGrassAction(Action):
    def execute(self, map):
        free_cells = [
            (x, y)
            for x in range(map.width)
            for y in range(map.height)
            if map.is_cell_empty(x, y)
        ]
        if len(map.resources) < 5 and free_cells:
            x, y = random.choice(free_cells)
            map.add_entity(Grass(x, y))


