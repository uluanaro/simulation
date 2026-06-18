import collections


def find_path_to_target(start_x, start_y, map, target_type, is_passable):
    queue = collections.deque()
    queue.append((start_x, start_y))

    visited = set()
    visited.add((start_x, start_y))
    came_from = {}

    while queue:
        x, y = queue.popleft()
        entity = map.get_entity_at(x, y)
        if isinstance(entity, target_type):
            path = []
            current = (x, y)
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if map.is_within_bounds(new_x, new_y) and (new_x, new_y) not in visited:
                neighbor_entity = map.get_entity_at(new_x, new_y)
                if is_passable(neighbor_entity):
                    visited.add((new_x, new_y))
                    came_from[(new_x, new_y)] = (x, y)
                    queue.append((new_x, new_y))
    return None
