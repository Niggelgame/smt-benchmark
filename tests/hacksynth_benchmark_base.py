
import os
import subprocess
from environment import environment
from tests.test_base import TestBase
import utils


class HackSynthBenchmark_Base(TestBase):
    def get_git_info(self):
        return {
            "branch": "main",
            "commit": "latest",
        }
    
    def get_test_runner(self):
        return "bitvec_benchmarks/hackdel.py"
    
    def get_params(self):
        return []
    
    def get_info(self):
        return {
            "name": "hacksynth-benchmark",
            "description": "hacksynth benchmark",
            "required_environment": [],
        }
    
    def clone_to_temp(self):
        # clone the repository

        temp_dir = utils.get_temp_dir()
        test_name = self.get_info()["name"]

        repo_path = os.path.join(temp_dir, f"synth_{test_name}")

        # if the directory already exists, remove it
        if os.path.exists(repo_path):
            # really pay attention here
            os.system(f'rm -rf "{repo_path}"')
        
        # clone the repo into the temp directory
        script = f"""git clone https://github.com/shack/synth.git {repo_path}"""

        try:
            os.system(script)
        except Exception as e:
            self.log(f"Error cloning repository: {e}", 0)
            return

        # checkout the specified branch / commit
        commit = self.get_git_info()["commit"]
        branch = self.get_git_info()["branch"]
        if commit is None or commit == "latest":
            script = f"""cd {repo_path} && git checkout {branch}"""
        else:
            script = f"""cd {repo_path} && git checkout {commit}"""
        try:
            os.system(script)
        except Exception as e:
            self.log(f"Error checking out commit: {e}", 0)
            return
        
        return repo_path
        
    def get_test_cases(self, repo_path):
            python = utils.get_own_python_executable()

            # get all test cases
            script = f"""cd {repo_path} && {python} {self.get_test_runner()} -T"""
            self.log(f"Running command: {script}", 2)
            try:
                p = subprocess.run(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except Exception as e:
                self.log(f"Error: {e}", 1)
                results = "error"
                return
            output = p.stdout.decode('utf-8')
            # split output by comma for each test case as specified by "-T"
            test_cases = output.strip().split(",")
            return test_cases

    def success_output(self, bench_path, testcase):
        pass

    def execute_tests(self, path):
        results = {}
        # run the tests
        try:
            # get own python executable which includes z3
            python = utils.get_own_python_executable()

            test_cases = self.get_test_cases(path)
            
            # run the tests
            for test_case in test_cases:
                self.log(f"Running test: {test_case}", 1)
                with utils.timer() as elapsed:
                    script = f"""cd {path} && timeout -s SIGKILL {utils.get_test_timeout()} {python} {self.get_test_runner()} -t {test_case} {' '.join(self.get_params())}"""
                    self.log(f"Running command: {script}", 2)
                    try:
                        p = subprocess.run(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    except Exception as e:
                        self.log(f"Error: {e}", 1)
                        results[test_case] = "error"
                        return
                    output = p.stdout.decode('utf-8')

                    # timeout code predefined by the system
                    if utils.is_returncode_timeout(p.returncode):
                        self.log(f"timed out", 1)
                        results[test_case] = "timeout"
                    else:
                        self.log(f"Output: {output}", 3)
                        results[test_case] = elapsed()
                        self.success_output(path, test_case)
            
            return results
        finally:
            if not environment["KEEP_TEMP"]:
                # remove the temp directory
                os.system(f'rm -rf "{path}"')

    def run_test(self):
        path = self.clone_to_temp()

        return self.execute_tests(path)
        
        