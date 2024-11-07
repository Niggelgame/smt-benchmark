from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthStdHackdelBenchmark(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthStdHackdelBenchmarkBrahmaPaper"
        return base
    
    def get_params(self):
        return super().get_params() + ["synth:brahma-paper"]
    
    def get_test_set(self):
        return 'hackdel'
    
def create_test():
    return HacksynthStdHackdelBenchmark()