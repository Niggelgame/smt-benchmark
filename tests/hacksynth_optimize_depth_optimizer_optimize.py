from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthOptimizeDepthOptimizerOptimize(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthOptimizeDepthOptimizerOptimize"
        base["description"] = "hacksynth benchmark, with optimizer for depth using z3 Optimize"
        return base
    
    def get_test_set(self):
        return 'hackdel'
    
    def get_git_info(self):
        base = super().get_git_info()
        base["branch"] = "main"
        return base
    

    def get_params(self):
        # Fixed length of 8, as this is the maximal length required
        return ["synth:opt-cegis", "--synth.size_range 8 8", "synth.optimizer:depth"]
    
def create_test():
    return HacksynthOptimizeDepthOptimizerOptimize()