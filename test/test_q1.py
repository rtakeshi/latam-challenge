import pytest
import sys
import os
from datetime import datetime

#adding src directory to sys path
current_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.join(current_directory, '..', 'src')
sys.path.append(src_directory)



from q1_memory import q1_memory
from q1_time import q1_time

TEST_DATA_DIR = "../data/test/test_data.csv"

def test_q1_memory():
    result = q1_memory(TEST_DATA_DIR)
    expected_result = [
        (datetime(2023, 7, 13).date(), "rachelyoung"),
        (datetime(2023, 9, 6).date(), "annathompson"),
        (datetime(2023, 2, 10).date(), "jeffrey20"),
        (datetime(2022, 11, 8).date(), "joel53"),
        (datetime(2023, 2, 13).date(), "joel53"),
        (datetime(2023, 4, 21).date(), "williamking"),
        (datetime(2023, 7, 30).date(), "wrightdana"),
        (datetime(2023, 1, 15).date(), "jennifer56"),
        (datetime(2023, 9, 7).date(), "elizabeth58"),
        (datetime(2022, 11, 29).date(), "joel53")
    ]
    assert result == expected_result


def test_q1_time():
    result = q1_time(TEST_DATA_DIR)
    expected_result = [
        (datetime(2023, 7, 13).date(), "rachelyoung"),
        (datetime(2023, 9, 6).date(), "annathompson"),
        (datetime(2023, 2, 10).date(), "jeffrey20"),
        (datetime(2022, 11, 8).date(), "joel53"),
        (datetime(2023, 2, 13).date(), "joel53"),
        (datetime(2023, 4, 21).date(), "williamking"),
        (datetime(2023, 7, 30).date(), "wrightdana"),
        (datetime(2023, 1, 15).date(), "jennifer56"),
        (datetime(2023, 9, 7).date(), "elizabeth58"),
        (datetime(2022, 11, 29).date(), "joel53")
    ]

    assert result == expected_result
