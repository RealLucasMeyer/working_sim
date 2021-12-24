from numpy.random import default_rng

class Worker:

    def __init__(self, worker_id, competency):
        self.career_length = 10
        self.worker_id = worker_id
        self.competency = competency

    def work(self):
        rng = default_rng()
        return rng.normal(loc=self.competency)