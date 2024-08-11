from tests.cvc5_8bit_benchmark import Cvc5_8bitBenchmark
import utils

class Cvc5_32bitBenchmark(Cvc5_8bitBenchmark):
    def get_info(self):
        return {
            "name": "cvc5-32bit-benchmark",
            "description": "cvc5 SyGuS 32-bit benchmarks",
            "required_environment": ["CVC5_PATH"],
        }

    def get_files_dir(self):
        return utils.get_root_path() + "/resources/sygus-hd-32bit"
    

def create_test():
    return Cvc5_32bitBenchmark()