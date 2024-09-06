from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthOptimizeDepthOptimizer(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthOptimizeDepthOptimizer"
        base["description"] = "hacksynth benchmark, with optimizer for depth using z3 Optimize"
        return base
    
    def get_test_runner(self):
        return 'bitvec_benchmarks/hackdel.py'
    
    def get_git_info(self):
        base = super().get_git_info()
        base["branch"] = "main"
        return base
    
    def get_solver_name(self):
        return 'synth_n_optimize_temp'

    def get_params(self):
        # Fixed length of 8, as this is the maximal length needed
        return super().get_params() + ["-l 8", "-L 8", f"-s {self.get_solver_name()}"]
        
    def run_test(self):
        path = self.clone_to_temp()

        results = {}
        
        optimizers = ["simple_depth_optimization", "iterated_depth_optimization"]

        for optimizer in optimizers:
            # replace the optimization case
            with open(f"{path}/synth_n_optimize.py", "r+") as file:
                data = file.read()
            
            with open(f"{path}/{self.get_solver_name()}.py", "w") as file:
                file.write(data.replace("{{CAN_BE_REPLACED_BY_BENCHMARK}}", optimizer))

            results[optimizer] = self.execute_tests(path)
        
        return results
    
def create_test():
    return HacksynthOptimizeDepthOptimizer()