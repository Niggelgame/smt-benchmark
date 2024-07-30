from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthStdHackdelBenchmark(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthStdHackdelBenchmark"
        return base
    
    def get_test_runner(self):
        return 'hackdel.py'
    
def create_test():
    return HacksynthStdHackdelBenchmark()