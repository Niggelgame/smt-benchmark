from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

# benchmark files used to quickly rebench individual test cases

from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthHackdelFullSygus(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthHackdelFullSygus"
        base["description"] = "hacksynth benchmark, test cases are SyGuS benchmarks"
        return base
    
    def get_test_runner(self):
        return 'bitvec_benchmarks/from_sygus_spec_hackdel.py'
    

    def get_params(self):
        return super().get_params() + ['-c SET']
    
    def get_test_cases(self, repo_path):
        return ['p19_d1', 'p19_d5']
    
def create_test():
    return HacksynthHackdelFullSygus()