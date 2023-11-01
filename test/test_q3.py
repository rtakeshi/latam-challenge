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
        ("yhernandez", 20),
        ("alexisdavis", 19),
        ("james07", 19),
        ("omar90", 17),
        ("chadthompson", 16),
        ("elizabethcampbell", 15),
        ("walkerkimberly", 14),
        ("daniel84", 13),
        ("smithchristina", 13),
        ("tracy04", 13)
]

    assert result == expected_result



def test_q3_time():
    result = q3_time(TEST_DATA_DIR)

    expected_result  = [
        ("yhernandez", 20),
        ("alexisdavis", 19),
        ("james07", 19),
        ("omar90", 17),
        ("chadthompson", 16),
        ("elizabethcampbell", 15),
        ("walkerkimberly", 14),
        ("daniel84", 13),
        ("smithchristina", 13),
        ("tracy04", 13)
]

    assert result == expected_result