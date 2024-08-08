from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthOptimizeDepthOptimizer(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthOptimizeDepthOptimizer"
        base["description"] = "hacksynth benchmark, with optimizer for depth using z3 Optimize"
        return base
    
    def get_test_runner(self):
        return 'hackdel.py'
    
    def get_git_info(self):
        base = super().get_git_info()
        base["branch"] = "main"
        return base

    def get_params(self):
        # Fixed length of 8, as this is the maximal length needed
        return super().get_params() + ["-l 8", "-L 8", "-s synth_n_optimize"]
    
    def clone_to_temp(self):
        path = super().clone_to_temp()

        # replace the optimization case
        with open(f"{path}/synth_n_optimize.py", "r+") as file:
            data = file.read()
            file.seek(0)
            file.write(data.replace("{{CAN_BE_REPLACED_BY_BENCHMARK}}", "simple_depth_optimization"))
        
        return path
    
def create_test():
    return HacksynthOptimizeDepthOptimizer()