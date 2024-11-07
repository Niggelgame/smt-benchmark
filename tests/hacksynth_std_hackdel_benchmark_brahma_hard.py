from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthStdHackdelBenchmark(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthStdHackdelBenchmarkBrahma"
        return base
    
    def get_run_params(self):
        return super().get_run_params() + ["--difficulty 40"]

    def get_params(self):
        return ["synth:brahma-iterate"]
    
    def get_test_set(self):
        return 'hackdel'
    
def create_test():
    return HacksynthStdHackdelBenchmark()