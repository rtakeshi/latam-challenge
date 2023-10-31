import pytest


from ..src.q1_memory import q1_memory
from ..src.q1_time import q1_time

#testing function for q1_memory
def test_q1_memory_test():
    result = q1_memory()

    #define the expected result for dataset
    expected_result = 42 

    # assert to verify if it will pass
    assert result == expected_result



def test_q1_time():
    result = q1_time()

    expected_result = 42

    assert result == expected_result