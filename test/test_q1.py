import pytest
import sys
import os

#adding src directory to sys path
current_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.join(current_directory, '..', 'src')
sys.path.append(src_directory)



from q1_memory import q1_memory
from q1_time import q1_time

TEST_DATA_DIR = "../data/test/test_data.csv"

#testing function for q1_memory
def test_q1_memory():
    result = q1_memory(TEST_DATA_DIR)
    

    expected_result = [
        ("2023-07-13", "katherinepatel"),
        ("2023-02-13", "joel53"),
        ("2022-11-08", "dennisemily"),
        ("2023-09-07", "rachelyoung"),
        ("2023-04-21", "darleneswanson"),
        ("2023-09-06", "dennisemily"),
        ("2023-09-18", "jeffrey20"),
        ("2023-01-15", "annathompson"),
        ("2022-11-29", "hernandezrachel"),
        ("2023-07-30", "katherinepatel")
]

    assert result == expected_result



def test_q1_time():
    result = q1_time(TEST_DATA_DIR)

    expected_result = [
        ("2023-07-13", "katherinepatel"),
        ("2023-02-13", "joel53"),
        ("2022-11-08", "dennisemily"),
        ("2023-09-07", "rachelyoung"),
        ("2023-04-21", "darleneswanson"),
        ("2023-09-06", "dennisemily"),
        ("2023-09-18", "jeffrey20"),
        ("2023-01-15", "annathompson"),
        ("2022-11-29", "hernandezrachel"),
        ("2023-07-30", "katherinepatel")
]

    assert result == expected_result