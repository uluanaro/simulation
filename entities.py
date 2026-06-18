import collections
from abc import ABC, abstractmethod

from path_finding import find_path_to_target


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
    def make_move(self, map):
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
        path = find_path_to_target(
            self.x, self.y, map,
            target_type=Grass,
            is_passable=lambda e: e is None or isinstance(e, Grass))
        if path is None:
            pass
        else:
            next_x, next_y = path[0]
            next_entity = map.get_entity_at(next_x, next_y)
            if isinstance(next_entity, Grass):
                map.remove_entity(next_entity)
            map.remove_entity(self)
            self.x, self.y = next_x, next_y
            map.add_entity(self)

class Predator(Creature):
    def __init__(self, x, y, hp, speed, attack_power):
        super().__init__(x, y, hp, speed)
        self.attack_power = attack_power

    def make_move(self, map):
        path = find_path_to_target(
            self.x, self.y, map,
            target_type=Herbivore,
            is_passable=lambda e: not isinstance(e, (Rock, Tree, Predator)))
        print(f"Хищник ({self.x},{self.y}): path={path}")
        if path is None:
            pass
        elif len(path) == 1:
            print("АТАКА!")

            next_x, next_y = path[0]
            next_entity = map.get_entity_at(next_x, next_y)
            next_entity.hp -= self.attack_power
            if next_entity.hp <= 0:
                map.remove_entity(next_entity)
        else:
            next_x, next_y = path[0]
            map.remove_entity(self)
            self.x, self.y = next_x, next_y
            map.add_entity(self)