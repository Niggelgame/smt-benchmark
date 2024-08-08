from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthDownscalingCegis(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthDownscalingCegis"
        base["description"] = "hacksynth benchmark, with downscaling, where second stage uses cegis"
        return base
    
    def get_test_runner(self):
        return 'hackdel.py'
    
    def get_git_info(self):
        base = super().get_git_info()
        base["branch"] = "main"
        return base

    def get_params(self):
        return super().get_params() + ["-s synth_constants_cegis_stage"]
    
def create_test():
    return HacksynthDownscalingCegis()