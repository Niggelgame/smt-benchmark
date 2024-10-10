from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthStdHackdelBenchmark(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthStdHackdelBenchmarkBrahma"
        return base
    
    def get_params(self):
        return super().get_params() + ["-s synth_brahma -x"]
    
    def get_test_runner(self):
        return 'bitvec_benchmarks/hackdel.py'
    
def create_test():
    return HacksynthStdHackdelBenchmark()