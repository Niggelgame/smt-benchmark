from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class SampleHacksynthBench(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "sample-hacksynth-bench"
        return base
    
def create_test():
    return SampleHacksynthBench()