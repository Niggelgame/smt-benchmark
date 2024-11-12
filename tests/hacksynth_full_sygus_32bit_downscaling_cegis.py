from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthHackdelFullSygus(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthHackdelFullSygusDownscaling32"
        base["description"] = "hacksynth benchmark, test cases are SyGuS benchmarks"
        return base
    
    def get_test_set(self):
        return 'hackdel-sygus'
    
    def get_run_params(self):
        return super().get_run_params() + ["--const_mode SET"]

    def get_set_params(self):
        return super().get_set_params() + ["--set.bit_width 32"]

    def get_params(self):
        return ["synth:downscale-synth", "--synth.constant_finder_use_cegis"]
    
def create_test():
    return HacksynthHackdelFullSygus()