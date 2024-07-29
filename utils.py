from contextlib import contextmanager
import os
import sys
import time
from environment import environment

def get_root_path():
    return sys.path[0]

def get_temp_dir():
    return os.path.join(get_root_path(), "temp")

def get_own_python_executable():
    return sys.executable

@contextmanager
def timer():
    start = time.perf_counter_ns()
    yield lambda: time.perf_counter_ns() - start


def get_test_timeout():
    if "TIMEOUT" in environment:
        return environment["TIMEOUT"]
    return "3600s"
    