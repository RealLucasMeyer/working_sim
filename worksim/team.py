class Team:
    def __init__(self):
        self.workers = []  # list of Worker objects

    def hire(self, worker):
        self.workers.append(worker)

    def fire(self, pos):
        self.workers.pop(pos)
