from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base

class HacksynthRulerBool(HackSynthBenchmark_Base):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthRulerBool"
        return base

    def get_test_cases(self, repo_path):
        # Ruler tests are a bit special. Run all the tests at once 
        return ['""']
    
    def get_test_set(self):
        return 'ruler-bool'
    
    
def create_test():
    return HacksynthRulerBool()