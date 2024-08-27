import json
from tests.hacksynth_benchmark_base import HackSynthBenchmark_Base


class HackSynthBenchmarkDownscaling_Base(HackSynthBenchmark_Base):
    def __init__(self) -> None:
        super().__init__()
        self.downscaling_times = {}

    def success_output(self, bench_path, testcase):
        json_path = bench_path + f"/{testcase}.json"
        # try to read test case statistics file
        try:
            with open(json_path, "r") as f:
                # array of runs
                json_data = json.load(f)
                
                downscaled_synth_time = 0
                finding_constants_time = 0
                other_synth_time = 0

                index = 0

                # get until first run, in which there is no "_transformed" variable inside; this is the upscaling run
                while index < len(json_data):
                    run = json_data[index]
                    assert len(run["iterations"]) > 0
                    # if this is the upscaling run of FA, then there is no "prg" property, as it is inserted by cegis
                    if (not "prg" in run["iterations"][0]) or "_transformed" not in run["iterations"][0]["prg"]:
                        break

                    downscaled_synth_time += run["time"]
                    index += 1
                
                # this run must be the upscaling/constant finding run, if there was at least one downscaled run
                if index == 0:
                    other_synth_time = sum([run["time"] for run in json_data])
                else:
                    finding_constants_time = json_data[index]["time"]
                    if index+1 < len(json_data):
                        other_synth_time = sum([run["time"] for run in json_data[index+1:]])

                self.downscaling_times[testcase] = {
                    "downscaled_synth_time": downscaled_synth_time,
                    "finding_constants_time": finding_constants_time,
                    "other_synth_time": other_synth_time
                }
        except FileNotFoundError:
            self.log(f"Warning: Stats File {json_path} not found", 1)
        

    def get_params(self):
        return super().get_params() + ["--stats"]

    def run_test(self):
        results = super().run_test()
        result = {
            "shell_times": results,
            "downscaling_times": self.downscaling_times
        }
        return result

