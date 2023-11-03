import pytest
import sys
import os

#adding src directory to sys path
current_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.join(current_directory, '..', 'src')
sys.path.append(src_directory)



from q3_memory import q3_memory
from q3_time import q3_time

TEST_DATA_DIR = "../data/test/test_data.csv"

#testing function for q3_memory
def test_q3_memory():
    result = q3_memory(TEST_DATA_DIR)


    expected_result  = [
        ('@hernandezrachel', 11),
        ('@lisa42', 10), 
        ('@hayley31', 9), 
        ('@wrightdana', 8), 
        ('@rachelyoung', 7), 
        ('@rodriguezvictoria', 7), 
        ('@amyjohnson', 6), 
        ('@darleneswanson', 6), 
        ('@joel53', 6), 
        ('@williamking', 6)
    ]


    assert result == expected_result



def test_q3_time():
    result = q3_time(TEST_DATA_DIR)

    expected_result  = [
        ('@hernandezrachel', 11),
        ('@lisa42', 10), 
        ('@hayley31', 9), 
        ('@wrightdana', 8), 
        ('@rachelyoung', 7), 
        ('@rodriguezvictoria', 7), 
        ('@amyjohnson', 6), 
        ('@darleneswanson', 6), 
        ('@joel53', 6), 
        ('@williamking', 6)
    ]

    assert result == expected_result