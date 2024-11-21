from tests.hacksynth_solver_comp import HacksynthSolverComp

class HacksynthSolverComp32(HacksynthSolverComp):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthSolverComp32"
        return base
    
    def get_set_params(self):
        return super().get_set_params() + ["--set.bit_width 32"]

    def run_test(self):
        solvers = ["yices"]

        path = self.clone_to_temp()

        results = {}

        for solver in solvers:
            self.active_solver = solver

            results[solver] = self.execute_tests(path)
        
        return results
    
    
def create_test():
    return HacksynthSolverComp32()