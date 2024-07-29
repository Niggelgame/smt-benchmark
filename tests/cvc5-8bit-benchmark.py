from tests.test_base import TestBase
import utils
from environment import environment


class Cvc5_8bitBenchmark(TestBase):
    def get_info(self):
        return {
            "name": "cvc5-8bit-benchmark",
            "description": "cvc5 SyGuS 8-bit benchmarks",
            "required_environment": ["CVC5_PATH"],
        }



    def run_test(self):
        import os
        import subprocess

        cvc5_path = environment["CVC5_PATH"]


        files_dir = utils.get_root_path() + "/resources/sygus-hd-8bit"
        # get files in directory

        results = {}

        files = os.listdir(files_dir)
        ordered_files = sorted(files)
        
        for filename in ordered_files:
            full_path = os.path.join(files_dir, filename)

            self.log(f"Running test: {filename}", 1)

            with utils.timer() as elapsed:
                cmd = f"{cvc5_path} {full_path}"
                timeout_cmd = f"timeout -s SIGKILL {utils.get_test_timeout()} {cmd}"
                self.log(f"Running command: {timeout_cmd}", 2)
                try:
                    p = subprocess.run(timeout_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except Exception as e:
                    self.log(f"Error: {e}", 1)
                    results[filename] = "error"
                    continue
                output = p.stdout.decode('utf-8')

                if utils.is_returncode_timeout(p.returncode):
                    self.log(f"{filename} timed out", 1)
                    results[filename] = "timeout"
                else:
                    self.log(f"Output: {output}", 3)
                    results[filename] = elapsed()

        return results


def create_test():
    return Cvc5_8bitBenchmark()