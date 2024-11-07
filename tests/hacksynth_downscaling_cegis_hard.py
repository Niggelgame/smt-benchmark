from tests.hacksynth_benchmark_downscaling_base import HackSynthBenchmarkDownscaling_Base

class HacksynthDownscalingCegis(HackSynthBenchmarkDownscaling_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthDownscalingCegisHard"
        base["description"] = "hacksynth benchmark, with downscaling, where second stage uses cegis"
        return base
    
    def get_test_set(self):
        return 'hackdel'
    
    def get_git_info(self):
        base = super().get_git_info()
        base["branch"] = "main"
        return base

    def get_run_params(self):
        return super().get_run_params() + ["--difficulty 40 --const_mode FREE"]

    def get_params(self):
        return ["synth:downscale-synth", "--synth.constant_finder_use_cegis"]
    
def create_test():
    return HacksynthDownscalingCegis()