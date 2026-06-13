from abc import ABC, abstractmethod
class Action(ABC):

    @abstractmethod
    def execute(self, map):
        pass

class PrintMapAction(Action):
    def execute(self, map):
        result = len(map.get_all_entities())
        print(result)