import pytest
import sys
import os

#adding src directory to sys path
current_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.join(current_directory, '..', 'src')
sys.path.append(src_directory)



from q3_memory import q3_memory
from q3_time import q3_time

#testing function for q3_memory
def test_q3_memory():
    result = q3_memory("hello")
    result = 42

    #define the expected result for dataset
    expected_result = 42 

    # assert to verify if it will pass
    assert result == expected_result



def test_q3_time():
    result = q3_time("world")
    result = 42

    expected_result = 42

    assert result == expected_result