class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = {}

    def add_entity(self, entity):
        if (entity.x, entity.y) in self.cells.keys():
            print("Клетка уже занята")
        else:
            self.cells[(entity.x, entity.y)] = entity

    def remove_entity(self, entity):
        if (entity.x, entity.y) in self.cells.keys():
            del self.cells[(entity.x, entity.y)]

    def get_entity_at(self, x, y):
        return self.cells.get((x, y))

    def is_cell_empty(self, x, y):
        return (x, y) not in self.cells

    def is_within_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get_all_entities(self):
        return list(self.cells.values())