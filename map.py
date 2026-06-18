from entities import Creature, Grass, Rock, Tree


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.creatures = {}
        self.resources = {}
        self.static_objects = {}

    def add_entity(self, entity):
        if isinstance(entity, Creature):
            if (entity.x, entity.y) in self.creatures:
                print("Клетка уже занята существом")
            else:
                self.creatures[(entity.x, entity.y)] = entity
        elif isinstance(entity, Grass):
            self.resources[(entity.x, entity.y)] = entity
        elif isinstance(entity, (Rock, Tree)):
            self.static_objects[(entity.x, entity.y)] = entity

    def remove_entity(self, entity):
        if isinstance(entity, Creature):
            if (entity.x, entity.y) in self.creatures:
                del self.creatures[(entity.x, entity.y)]
        elif isinstance(entity, Grass):
            if (entity.x, entity.y) in self.resources:
                del self.resources[(entity.x, entity.y)]
        elif isinstance(entity, (Rock, Tree)):
            if (entity.x, entity.y) in self.static_objects:
                del self.static_objects[(entity.x, entity.y)]

    def get_entity_at(self, x, y):
        return (self.creatures.get((x, y)) or
                self.resources.get((x, y)) or
                self.static_objects.get((x, y)))

    def is_cell_empty(self, x, y):
        return (x, y) not in self.creatures and (x, y) not in self.static_objects

    def is_within_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get_all_entities(self):
        return list(self.creatures.values())

    def get_all_for_render(self):
        all_entities = {}
        all_entities.update(self.static_objects)
        all_entities.update(self.resources)
        all_entities.update(self.creatures)
        return all_entities