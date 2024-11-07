from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthStdHackdelBenchmark(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthStdHackdelBenchmark16"
        return base
    
    def get_test_set(self):
        return 'hackdel'
    
    def get_run_params(self):
        return super().get_run_params() + ["--difficulty 40 --const_mode FREE"]

    def get_set_params(self):
        return super().get_set_params() + ["--set.bit_width 16"]
    
def create_test():
    return HacksynthStdHackdelBenchmark()