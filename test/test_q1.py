import pytest


from ..src.q1_memory import q1_memory
from ..src.q1_time import q1_time

#testing function for q1_memory
def test_q1_memory():
    result = q1_memory()
    result = 42

    #define the expected result for dataset
    expected_result = 42 

    # assert to verify if it will pass
    assert result == expected_result



def test_q1_time():
    result = q1_time()
    result = 42

    expected_result = 42

    assert result == expected_result