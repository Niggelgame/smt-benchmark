from contextlib import contextmanager
import os
import sys
import time
from environment import environment

import matplotlib.pyplot as plt

font_size = 10

def get_root_path():
    return sys.path[0]

def get_temp_dir():
    return os.path.join(get_root_path(), "temp")

def get_own_python_executable():
    return sys.executable

def is_returncode_timeout(returncode):
    return returncode == 137 or returncode == -9 or returncode == 124

@contextmanager
def timer():
    start = time.perf_counter_ns()
    yield lambda: time.perf_counter_ns() - start


def get_test_timeout():
    if "TIMEOUT" in environment:
        return environment["TIMEOUT"]
    return "3600s"

def draw_plot(data, pos, output):
    """Create a violin plot
    
    data: nested array of data points, for each violin plot point in the array
    pos: array of x-axis positions for each violin plot, e. g. leave out space between test results
    output: file name of the output file
    """
    fig, ax = plt.subplots()
    ax.violinplot(data, pos, points=100, widths=0.3, showmeans=True, showextrema=True, showmedians=True, bw_method=0.5)
    ax.set_yscale("log")
    ax.set_title("Results", fontsize=font_size)
    plt.show()