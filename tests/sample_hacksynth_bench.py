from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

# Disabled Test case.
class SampleHacksynthBench(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "sample-hacksynth-bench"
        base["enabled"] = False
        return base
    
def create_test():
    return SampleHacksynthBench()