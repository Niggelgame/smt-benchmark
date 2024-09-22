from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthSolverComp(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthSolverComp"
        return base
    
    def get_solver_file(self):
        return 'synth_n_copy'
    
    def get_test_runner(self):
        return 'bitvec_benchmarks/hackdel.py'
    
    def get_params(self):
        return super().get_params() + [f"-s {self.get_solver_file()}"]
    
    def run_test(self):
        solver_methods = ["solve_external_yices", "solve_z3", "solve_external_bitwuzla", "solve_external_cvc5", "solve_external_z3"]

        to_be_replaced = "solve=solve_z3"
        path = self.clone_to_temp()

        results = {}

        for solver in solver_methods:
            solver_file = 'synth_n.py'

            with open(f"{path}/{solver_file}", "r") as file:
                data = file.read()
            
            new_data = data.replace(to_be_replaced, f"solve={solver}")

            with open(f"{path}/{self.get_solver_file()}.py", "w") as file:
                file.write(new_data)

            results[solver] = self.execute_tests(path)
        
        return results

    
    
def create_test():
    return HacksynthSolverComp()