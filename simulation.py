import time


class Simulation():
    def __init__(self, map, init_actions, turn_actions):
        self.map = map
        self.turn_count = 0
        self.init_actions = init_actions
        self.turn_actions = turn_actions
        self.running = False

        for action in self.init_actions:
            action.execute(self.map)

    def next_turn(self):
        self.turn_count += 1
        for action in self.turn_actions:
            action.execute(self.map)

    def start_simulation(self):
        self.running = True
        while self.running:
            self.next_turn()
            time.sleep(0.5)

    def pause_simulation(self):
        self.running = False