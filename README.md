# Benchmark / Testsuite for SMT based program synthesis



## Running the tests

1. Checkout the repository
2. Install required dependencies (possibly in a virtual environment*)
```
pip install -r requirements.txt
```
3. Install required dependencies for the synthesis tools (e. g. CVC5) -> z3 is auto-installed with this package
4. Copy the `.env.sample` file to `.env` and adjust the parameters
5. Run the `test_runner.py`

\* Setting up venv: `python3 -m venv venv` and `source venv/bin/activate`


## Adding dependencies

Make sure to add the dependencies to the `requirements.txt` file. You can do this in the virtual environment by running the following command:

```
pip freeze > requirements.txt
```
