# Benchmark / Testsuite for SMT based program synthesis



## Running the tests

1. Checkout the repository
2. Install required dependencies (possibly in a virtual environment*)
```
pip install -r requirements.txt
```
3. Install required dependencies for the synthesis tools (e. g. CVC5) -> z3 is auto-installed with this package
4. Copy the `.env.sample` file to `.env` and adjust the parameters
5. Run the `test_runner.py`.

\* Setting up venv: `python3 -m venv venv` and `source venv/bin/activate`

### Parameters

The following parameters can be set in the `.env` file:
| Parameter | Description | Default |
| --- | --- | --- |
| `TIMEOUT` | Timeout for each test in seconds, specified as the unix `timeout` command  | 3600s |
| `LOG_LEVEL` | Log level for the test runner. Higher->More detailed logging | `0` |
| `KEEP_TEMP` | Keep temporary files after the test run, as e. g. repo clones | `False` |
| `CVC5_PATH` | Path to the CVC5 binary | `unspecified` |

The following parameters can be set via the command line:
| Parameter | Description | Default |
| --- | --- | --- |
| `--benchmark / -b {Test case}` | Just run this test case. Comma separated for multiple tests  | `None` |
| `--output / -o {Output file}` | Write the results to this file | `None` |
| `--intermediate_output / -i` | Write intermediate results to the output file | `False` |
| `--repeats / -r {number}` | Repeat the tests this number of times | `1` |

-> To log the outputs of the benchmark runs to a file, use `{run command} > logfile.txt 2>&1`

## Adding dependencies

Make sure to add the dependencies to the `requirements.txt` file. You can do this in the virtual environment by running the following command:

```
pip freeze > requirements.txt
```


## Creating a new test (suite)
1. Create a new file in the `tests` directory (if it is only a base for more tests, suffix it with '_base.py')
2. Implement the test as a class that inherits from `TestBase` and implements the `get_info` and `run` method. See the documentation of the `TestBase` class for more information. (e. g. check out the `tests/sample_hacksynth_bench.py`)


## Visualizing the results

The benchmark results are in the form of a JSON file. The `script` directory contains samples of how this data can be used to create visualizations using `matplotlib`.