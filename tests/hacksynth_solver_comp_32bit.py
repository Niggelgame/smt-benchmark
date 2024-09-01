from tests.hacksynth_solver_comp import HacksynthSolverComp

class HacksynthSolverComp32(HacksynthSolverComp):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthSolverComp32"
        return base
    
    def get_params(self):
        return super().get_params() + ["-b 32"]

    
    
def create_test():
    return HacksynthSolverComp32()