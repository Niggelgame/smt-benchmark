import os
import environment


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(prog="test_runner")
    parser.add_argument("-b", "--benchmark", help="Run a specific benchmark")
    return parser.parse_args()

def runner_log(msg, lvl):
        name = "MAIN"

        if lvl <= environment.environment["LOG_LEVEL"]:
            print(f"[{name}] {msg}")

def load_benchmark_module(benchmark):
    import importlib.util
    import sys
    spec = importlib.util.spec_from_file_location("module.benchmark", benchmark)
    benchmark_module = importlib.util.module_from_spec(spec)
    sys.modules["module.benchmark"] = benchmark_module
    spec.loader.exec_module(benchmark_module)
    return benchmark_module.create_test()


benchmark_results = {}

def run_benchmark(benchmark, arguments):
    benchmark = load_benchmark_module(benchmark)

    name = benchmark.get_info()["name"]
    runner_log(f"Running benchmark: {name}", 0)
    runner_log(f"Test Info: {benchmark.get_info()}", 1)

    # check for required environment variables
    required_environment = benchmark.get_info()["required_environment"]
    if required_environment is not None:
        for env in required_environment:
            if not env in environment.environment:
                runner_log(f"Missing required environment variable: {env}", 0)
                return

    results = benchmark.run_test()

    # append benchmark results
    if not name in benchmark_results:
         benchmark_results[name] = []
    benchmark_results[name].append(results)





def run():
    print("Starting Benchmark")
    # load the environment
    print("Loading environment")
    environment.load_environment()
    runner_log(f"Got environment {environment.environment}", 1)

    

    # parse additional arguments
    arguments = parse_args()

    tests_directory = os.path.join(os.path.dirname(__file__), "tests")

    # get all test files
    test_files = [os.path.join(tests_directory, f) for f in os.listdir(tests_directory) if f.endswith(".py")]

    # run a specific benchmark?
    if arguments.benchmark is not None:
        test = [file for file in test_files if arguments.benchmark in file]
        if len(test) == 0:
            runner_log(f"Could not find benchmark: {arguments.benchmark}", 0)
            return
        elif len(test) > 1:
            runner_log(f"Found multiple benchmarks with the name: {arguments.benchmark}", 0)
            return

        run_benchmark(test[0], arguments)
        return

    for benchmark in test_files:
        # base files are only used for inheritance
        if benchmark.endswith("_base.py"):
            continue
        run_benchmark(benchmark, arguments)

    
    

if __name__ == "__main__":
    run()
    print(benchmark_results)
