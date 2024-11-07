from tests.hacksynth_solver_comp import HacksynthSolverComp

class HacksynthSolverCompConstantModesFree(HacksynthSolverComp):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthSolverCompConstantModesFree"
        return base
    
    def get_test_set(self):
        return 'hackdel'
    
    def get_run_params(self):
        return super().get_run_params() + ["--const_mode FREE"]
    
    
def create_test():
    return HacksynthSolverCompConstantModesFree()