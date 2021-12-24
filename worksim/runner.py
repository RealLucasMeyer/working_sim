class WorkSimRunner:

    def __init__ (self):
        self.periods = 100

    def run(self):
        for t in range(self.periods):
            self.run_step(t)
    
    def run_step(self, t):
        print(f"Running period {t}")

