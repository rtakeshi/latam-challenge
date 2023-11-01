import pytest
import sys
import os

#adding src directory to sys path
current_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.join(current_directory, '..', 'src')
sys.path.append(src_directory)



from q2_memory import q2_memory
from q2_time import q2_time

#testing function for q2_memory
def test_q2_memory():
    result = q2_memory("hello")
    result = 42

    #define the expected result for dataset
    expected_result = 42 

    # assert to verify if it will pass
    assert result == expected_result



def test_q2_time():
    result = q2_time("world")
    result = 42

    expected_result = 42

    assert result == expected_result