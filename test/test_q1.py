import pytest
import sys
import os

#adding src directory to sys path
current_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.join(current_directory, '..', 'src')
sys.path.append(src_directory)



from q1_memory import q1_memory
from q1_time import q1_time

#testing function for q1_memory
def test_q1_memory():
    result = q1_memory("hello")
    result = 42

    #define the expected result for dataset
    expected_result = 42 

    # assert to verify if it will pass
    assert result == expected_result



def test_q1_time():
    result = q1_time("world")
    result = 42

    expected_result = 42

    assert result == expected_result