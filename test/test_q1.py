import pytest
import sys
import os

#adding src directory to sys path
current_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.join(current_directory, '..', 'src')
sys.path.append(src_directory)



from q1_memory import q1_memory
from q1_time import q1_time

TEST_DATA_DIR = "home/jovyan/work/data/test_data.csv"

#testing function for q1_memory
def test_q1_memory():
    result = q1_memory(TEST_DATA_DIR)
    

    expected_result = [
        ("2022-11-26", "alexisdavis"),
        ("2023-01-24", "alexisdavis"),
        ("2023-01-30", "alexisdavis"),
        ("2023-02-07", "craig48"),
        ("2023-03-31", "alexisdavis"),
        ("2023-05-26", "alexisdavis"),
        ("2023-06-23", "elizabethcampbell"),
        ("2023-07-25", "alexisdavis"),
        ("2023-07-31", "alexisdavis"),
    ]

    assert result == expected_result



def test_q1_time():
    result = q1_time(TEST_DATA_DIR)

    expected_result = [
        ("2022-11-26", "alexisdavis"),
        ("2023-01-24", "alexisdavis"),
        ("2023-01-30", "alexisdavis"),
        ("2023-02-07", "craig48"),
        ("2023-03-31", "alexisdavis"),
        ("2023-05-26", "alexisdavis"),
        ("2023-06-23", "elizabethcampbell"),
        ("2023-07-25", "alexisdavis"),
        ("2023-07-31", "alexisdavis"),
    ]

    assert result == expected_result