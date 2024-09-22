from tests.hacksynth_solver_comp import HacksynthSolverComp

class HacksynthSolverCompConstantModesFree(HacksynthSolverComp):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthSolverCompConstantModesSet"
        return base
    
    def get_solver_file(self):
        return 'synth_n_copy'
    
    def get_test_runner(self):
        return 'bitvec_benchmarks/hackdel.py'
    
    def get_params(self):
        return super().get_params() + ['-c SET']
    
    
def create_test():
    return HacksynthSolverCompConstantModesFree()