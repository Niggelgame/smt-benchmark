from tests.hacksynth_benchmark_downscaling_base import HackSynthBenchmarkDownscaling_Base

class HacksynthHackdelFullSygus(HackSynthBenchmarkDownscaling_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthHackdelFullSygusDownscaling64"
        base["description"] = "hacksynth benchmark, test cases are SyGuS benchmarks"
        return base
    
    def get_test_set(self):
        return 'hackdel_sygus'
    
    def get_run_params(self):
        return super().get_run_params() + ["--const_mode SET"]

    def get_set_params(self):
        return super().get_set_params() + ["--set.bit_width 64"]

    def get_params(self):
        return ["synth:downscale-synth", "--synth.constant_finder_use_cegis"]
    
def create_test():
    return HacksynthHackdelFullSygus()