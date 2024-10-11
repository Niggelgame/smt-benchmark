from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthStdHackdelBenchmark(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthStdHackdelBenchmarkBrahmaExact"
        return base
    
    def get_params(self):
        return super().get_params() + ["-s synth_brahma -x"]
    
    def get_test_runner(self):
        return 'bitvec_benchmarks/hackdel.py'
    
    def get_test_cases(self, repo_path):
        return ['p01', 'p02', 'p03', 'p04', 'p05', 'p06', 'p07', 'p08', 'p09', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20']

def create_test():
    return HacksynthStdHackdelBenchmark()