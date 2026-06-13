import collections
from abc import ABC, abstractmethod

from path_finding import find_path_to_grass


class Entity(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Creature(Entity):
    def __init__(self, x, y, hp, speed):
        super().__init__(x, y)
        self.hp = hp
        self.speed = speed

    @abstractmethod
    def make_move(self):
        pass

class Grass(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

class Rock(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

class Tree(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

class Herbivore(Creature):
    def __init__(self, x, y, hp, speed):
        super().__init__(x, y, hp, speed)

        def make_move(self, map):
            path = find_path_to_grass(self.x, self.y, map)
            if path is None:
                pass
            elif len(path) == 0:
                creature = map.get_entity_at(self.x, self.y)
                map.remove_entity(creature)
            else:
                map.remove_entity(self)
                (self.x, self.y) = path[0]
                map.add_entity(self)

class Predator(Creature):
    def __init__(self, x, y, hp, speed, attack_power):
        super().__init__(x, y, hp, speed)
        self.attack_power = attack_power

        def make_move(self):
            pass
