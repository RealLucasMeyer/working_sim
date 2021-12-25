from worksim import Worker
from worksim import Team
from numpy import default_rng

class WorkSimRunner:

    def __init__ (self):
        self.periods = 10
        self.team_size = 10
        self.current_worker_id = 0

        # Workers market contains all workers that we have ever seen
        self.workers_market = []

        # For now, let's start with just one team
        self.team = Team()

        # Instantiate a random number generator
        rng = default_rng()

        # Create a team of size team_size
        # Add workers both to the world and to the team
        for wid in range(self.team_size):
            c = rng.integers(low=1, high=10, endpoint=True)
            w = self.create_worker(c)
            self.team.hire(w)
    
    def create_worker(self, competency):
        w = Worker(worker_id=self.current_worker_id, competency=competency)
        self.workers_market.append(w)
        self.current_worker_id += 1
        return w

    def run(self):
        for t in range(self.periods):
            self.run_step(t)
    
    def run_step(self, t):
        print(f"Running period {t}")

        production_vector = []

        for w in self.team.workers:
            p = w.work()
            print(f"Worker {w.worker_id} with competency {w.competency} produced {p}")
            production_vector.append(p)
        
        production = sum(production_vector)
        print(f"Production this period was {production}")

        promo = production_vector.index(max(production_vector))
        fired = production_vector.index(min(production_vector))

        print(f"I will fire worker {fired} and promote worker {promo}")


        print(f"End of period {t}\n\n")



