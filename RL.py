from LL import LL

class RL():
    def __init__(self, levels=3):
        self.levels = levels
        self.list = [LL() for _ in range(self.levels)]

    def add(self, p, i):
        self.list[p].add(i)

    def remove(self, i):     
        for level in self.list:
            try:
                level.remove(i)
                break
            except ValueError:
                pass
