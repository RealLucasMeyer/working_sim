from worksim.worker import Worker
from numpy.random import default_rng

class WorkSimRunner:

    def __init__ (self):
        self.periods = 10
        self.n_workers = 10
        self.workers = []

        rng = default_rng()

        for w in range(self.n_workers):
            c = rng.integers(low=1, high=10, endpoint=True)
            self.workers.append(Worker(worker_id = w, competency = c))


    def run(self):
        for t in range(self.periods):
            self.run_step(t)
    
    def run_step(self, t):
        print(f"Running period {t}")

        production = []

        for w in self.workers:
            p = w.work()
            print(f"Worker {w.worker_id} with competency {w.competency} produced {p}")
            production.append(p)
        
        print(f"Production this period was {production}")

        promo = production.index(max(production))
        fired = production.index(min(production))

        print(f"I will fire worker {fired} and promote worker {promo}")


        print(f"End of period {t}\n\n")



