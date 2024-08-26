from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthDownscalingFA(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthDownscalingFA"
        base["description"] = "hacksynth benchmark, with downscaling, where second stage uses exists-forall"
        return base
    
    def get_test_runner(self):
        return 'bitvec_benchmarks/hackdel.py'
    
    def get_git_info(self):
        base = super().get_git_info()
        base["branch"] = "main"
        return base

    def get_params(self):
        return super().get_params() + ["-s synth_constants_fa_stage"]
    
def create_test():
    return HacksynthDownscalingFA()