from tests.hacksynth_benchmark_downscaling_base import HackSynthBenchmarkDownscaling_Base

class HacksynthHackdelFullSygus(HackSynthBenchmarkDownscaling_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthHackdelFullSygusDownscaling64"
        base["description"] = "hacksynth benchmark, test cases are SyGuS benchmarks"
        return base
    
    def get_test_runner(self):
        return 'bitvec_benchmarks/from_sygus_spec_hackdel_32bit.py'
    

    def get_params(self):
        return super().get_params() + ['-c SET', "-s synth_constants_cegis_stage"]
    
def create_test():
    return HacksynthHackdelFullSygus()