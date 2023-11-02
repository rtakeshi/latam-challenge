import pytest
import sys
import os

#adding src directory to sys path
current_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.join(current_directory, '..', 'src')
sys.path.append(src_directory)



from q3_memory import q3_memory
from q3_time import q3_time

TEST_DATA_DIR = "home/jovyan/work/data/test_data.csv"

#testing function for q3_memory
def test_q3_memory():
    result = q3_memory(TEST_DATA_DIR)


    expected_result  = [
        ('joel53', 6)
        ('jcole', 5)
        ('hernandezrachel', 5)
        ('amyjohnson', 4)
        ('darleneswanson', 4)
        ('hayley31', 4)
        ('jeffrey20', 4)
        ('lisa42', 4)
        ('williamking', 4)
        ('wrightdana', 4)
    ]

    assert result == expected_result



def test_q3_time():
    result = q3_time(TEST_DATA_DIR)

    expected_result  = [
        ('joel53', 6)
        ('jcole', 5)
        ('hernandezrachel', 5)
        ('amyjohnson', 4)
        ('darleneswanson', 4)
        ('hayley31', 4)
        ('jeffrey20', 4)
        ('lisa42', 4)
        ('williamking', 4)
        ('wrightdana', 4)
    ]

    assert result == expected_result