from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthStdHackdelBenchmark(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthStdHackdelBenchmark32"
        return base
    
    def get_test_runner(self):
        return 'hackdel.py'
    
    def get_params(self):
        return super().get_params() + ["-y 40 -c FREE", "-b 32"]
    
def create_test():
    return HacksynthStdHackdelBenchmark()