from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthHackdelExtendedSygus(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthHackdelExtendedSygus"
        base["description"] = "hacksynth benchmark, test cases are extended by restrictions from SyGuS benchmarks"
        return base
    
    def get_test_runner(self):
        return 'hackdel_sygus_spec.py'
    
def create_test():
    return HacksynthHackdelExtendedSygus()