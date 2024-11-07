from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthSolverComp(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthSolverComp"
        return base
    
    def get_test_set(self):
        return 'hackdel'
    
    def get_params(self):
        return super().get_params() + [f"synth.solver:{self.active_solver}"]
    
    def run_test(self):
        solvers = ["yices", "internal-z3", "bitwuzla", "cvc5", "external-z3"]

        path = self.clone_to_temp()

        results = {}

        for solver in solvers:
            self.active_solver = solver

            results[solver] = self.execute_tests(path)
        
        return results

    
    
def create_test():
    return HacksynthSolverComp()