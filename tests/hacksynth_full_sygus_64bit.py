from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthHackdelFullSygus(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthHackdelFullSygus64"
        base["description"] = "hacksynth benchmark, test cases are SyGuS benchmarks"
        return base
    
    def get_test_set(self):
        return 'hackdel-sygus'
    
    def get_run_params(self):
        return super().get_run_params() + ["--const_mode SET"]

    def get_set_params(self):
        return super().get_set_params() + ["--set.bit_width 64"]
    
def create_test():
    return HacksynthHackdelFullSygus()