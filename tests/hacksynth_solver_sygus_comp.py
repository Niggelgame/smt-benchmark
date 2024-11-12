from tests.hacksynth_solver_comp import HacksynthSolverComp

class HacksynthSolverSygusComp(HacksynthSolverComp):
    def get_info(self):
        base = super().get_info()
        base["name"] = "HacksynthSolverSygusComp"
        return base
    
    def get_test_set(self):
        return 'hackdel-sygus'
    
    def get_params(self):
        return super().get_params() + ['-c SET']
    

    
    
def create_test():
    return HacksynthSolverSygusComp()