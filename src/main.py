"""
main.py is starting file and for debug
"""

from datetime import time
from constants import CONNECTIONS
from tests import calculate_efficiency
from utils import load_data, generate_results, create_path, display_results, time_minutes_from_noon

if __name__ == "__main__":
    graph = load_data(CONNECTIONS)

    start_stop = "leśnica"
    end_stop = "księże małe"
    start_time = time_minutes_from_noon("7:30:00")
    algorithm = "d"
    option = "t"

    display_results(*create_path(*generate_results(graph, start_stop, end_stop, start_time, algorithm, option)))
    display_results(*create_path(*generate_results(graph, start_stop, end_stop, start_time, algorithm="a", option="t")))
    display_results(*create_path(*generate_results(graph, start_stop, end_stop, start_time, algorithm="a", option="p")))

    calculate_efficiency(graph, start_stop, end_stop, start_time)
